"""DLC/ folder (language-independent parts and 0010_KO only).

DLC/0010_KO/sceda*.s14, scedaex*.s14, scedaexce10/11/32/33.s14 are wrapped in an XOR stream over the WHOLE file (reference_mod MISC_DATA_FILES.md 2):
    state = (state * 0x6C078965 + 0x3039) mod 2^32   (rolled BEFORE each byte)
    out   = in ^ ((state >> 16) & 0xFF) ^ ((state >> 24) & 0xFF)
    initial state = DLC id + scenario number (transform is its own inverse)
The initial states below were recovered by brute force search over 0..6e7 (known plaintext: tier version u32 + 'SN14SCEXVER0001', MEAS);
the base-game files (sceda) share the state of the scedaex file with the same number (same keystream, verified by LWC magic after decoding).
DLC/DLCInfo*.s14 (45 files, 7..1100 B) and DLC/0011/gd_*.s14 (846 B each) use a different/unknown cipher (entropy ~8 bits) -> 미해결, listed only.
DLC/0003/*.wmv (movies) and DLC/0005/*.bin (archives, K4 scope) are not parsed here.
"""
import re
from . import s14
from .s14 import GAME

# scedaex<NN> initial state (DLC id + number)
STATE_EX = {9: 1198845, 10: 1198840, 11: 1198842, 12: 1198851, 13: 1198856, 14: 1198858, 15: 1198847, 16: 1198862, 17: 1198864, 18: 1198866,
            19: 1258173, 26: 1431509, 27: 1431514, 28: 1431521, 29: 1431509,
            150: 1431635, 151: 1431639, 152: 1431642, 153: 1431647, 154: 1431651}
# Installed Korean CE scenarios 10 and 11 share their PK counterparts’ initial states.
STATE_CE = {10: STATE_EX[10], 11: STATE_EX[11], 32: 4598982, 33: 4598993}


def xor_stream(data, state):
    out = bytearray(len(data))
    for i, b in enumerate(data):
        state = (state * 0x6C078965 + 0x3039) & 0xFFFFFFFF
        out[i] = b ^ ((state >> 16) & 0xFF) ^ ((state >> 24) & 0xFF)
    return bytes(out)


def dlc_scenarios():
    """[(file, tier, number, initial state)] for DLC/0010_KO."""
    res = []
    for p in sorted((GAME / 'DLC' / '0010_KO').glob('*.s14')):
        m = re.match(r'sceda(ex|exce)?(\d+)\.s14', p.name)
        num = int(m.group(2))
        kind = m.group(1)
        st = STATE_CE.get(num) if kind == 'exce' else STATE_EX.get(num)
        res.append((p.name, {None: 'base(51)', 'ex': 'PK(92)', 'exce': 'CE(102)'}[kind], num, st))
    return res


def load_dlc_scenario(file):
    """Decode a DLC scenario file and return an s14.Container-like object (header/body/version)."""
    for f, tier, num, st in dlc_scenarios():
        if f == file:
            break
    else:
        raise KeyError(file)
    raw = xor_stream((GAME / 'DLC' / '0010_KO' / file).read_bytes(), st)
    c = s14.Container.__new__(s14.Container)
    from . import lwc
    c.path = GAME / 'DLC' / '0010_KO' / file
    c.raw = raw
    c.blob_off = lwc.find_blob(raw)
    c.header = raw[:c.blob_off]
    c.body = lwc.decompress(raw, c.blob_off)
    c.version = c.header[0x1CB] if len(c.header) > 0x1CB else None
    return c


def dlc_info_files():
    return sorted(p.name for p in (GAME / 'DLC').glob('DLCInfo*.s14'))


def dlc_gd_files():
    return sorted(p.name for p in (GAME / 'DLC' / '0011').glob('gd_*.s14'))
