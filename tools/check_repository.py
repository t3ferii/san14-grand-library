"""Offline public-content and Markdown-link checks. No game installation required."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from mod_compat import validate


def markdown_prose(text):
    text = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', text, flags=re.M | re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def check(root=ROOT):
    errors = []
    files = [p for p in root.rglob('*') if p.is_file() and not any(x in p.relative_to(root).parts for x in ('.git', '__pycache__', '.venv'))]
    allowed_extensions = {'.md', '.py', '.ps1', '.java', '.json', '.yml', '.yaml'}
    allowed_names = {'.gitignore', '.gitattributes', 'LICENSE-CODE', 'CODEOWNERS'}
    blocked_dirs = {'cache', 'downloads', 'research', 'backup', 'reference_mod', 'dist', 'build'}
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() not in allowed_extensions and path.name not in allowed_names:
            errors.append(f'Unexpected public file: {rel}')
        if blocked_dirs & set(path.relative_to(root).parts): errors.append(f'Private output directory: {rel}')
        if path.stat().st_size > 3 * 1024 * 1024: errors.append(f'Large file needs manual curation: {rel}')
        try: text = path.read_text(encoding='utf-8-sig')
        except UnicodeError:
            errors.append(f'Non-text public file: {rel}'); continue
        if re.search(r'C:[\\/]Users[\\/](?!<)', text, re.I): errors.append(f'Personal absolute path: {rel}')
        if re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----', text):
            errors.append(f'Possible secret: {rel}')
        if path.suffix == '.json':
            try: json.loads(text)
            except ValueError as e: errors.append(f'JSON error: {rel}: {e}')
        if path.suffix == '.md':
            for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', markdown_prose(text)):
                if target.startswith(('#', 'http://', 'https://', 'mailto:')): continue
                local = unquote(target.split('#')[0])
                # Research prose sometimes contains array[index](argument) notation.
                if '/' not in local and '.' not in local and local != 'LICENSE-CODE': continue
                resolved = (path.parent / local).resolve()
                if resolved != root and root not in resolved.parents:
                    errors.append(f'Link escapes repository: {rel} -> {target}')
                elif not resolved.exists(): errors.append(f'Broken link: {rel} -> {target}')
    for path in (root / 'examples').glob('*.json'):
        try: validate(json.loads(path.read_text(encoding='utf-8')))
        except (ValueError, KeyError, TypeError) as e: errors.append(f'Manifest {path.name}: {e}')
    return files, errors


if __name__ == '__main__':
    files, errors = check()
    for error in errors: print(error)
    print(f'Public-content/link checks: {len(files)} files, {len(errors)} errors')
    raise SystemExit(bool(errors))
