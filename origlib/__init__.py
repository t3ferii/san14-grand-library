"""origlib - read the original San14 data files without parsing them again.

    import origlib
    origlib.load_fixdata()['trait']          # master tables: {key: [record dict]} (KO only)
    origlib.load_scenario(3)                 # Scenario; origlib.load_scenario(3, 'general') -> records
    origlib.msg(40044, 'msggame')            # message text (id = section*10000 + index)
    origlib.events('EventTutorial')          # EventFile: .events(), .speech(ev)
    origlib.load_map().cell(i)               # 220x220 map cell table
    origlib.load_bt()                        # behaviour trees (JBTP)
    origlib.rdb.open(name) / origlib.bin0005.open(n)    # archives (K4 modules; never `import *`)
CLI: python -m origlib tables|table <name>|scenario <id> <block>|msg <id>|find <text>|events|map|misc|dlc|rdb
Only the Korean data (0001_KO, 0010_KO, DLC/0010_KO) and language-independent folders are supported (user decision 2026-11-07).
"""
from . import s14, lwc, spec, fixdata, scenario, msg as _msg_mod, mapbin, misc0000, event as _event_mod, dlc
from . import rdb, bin0005
from .fixdata import load_fixdata, FixData
from .scenario import load_scenario, scenario_ids, Scenario
from .mapbin import load_map
from .misc0000 import load_bt
from .event import events, event_files
from .msg import find as find_text


def msg(id, name='msggame_exce', lang='KO'):
    """Message text by id (section*10000 + index). lang is fixed to KO."""
    return _msg_mod.msg(id, name, lang)


def lwc_decompress(data):
    return lwc.decompress(data)
