from collections import OrderedDict
from typing import Dict, List

from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED
from gendiff.formatters.formatter import formatter
from gendiff.parser import parse


def _process_keys(keys: List, data: Dict, status: str) -> Dict:
    diffs = {}
    for key in keys:
        diffs[key] = {
            "status": status,
            "diff": data.get(key),
        }
    return diffs


def _generate_diffs(data1: Dict, data2: Dict) -> Dict:
    diffs = {}

    added_keys = list(data2.keys() - data1.keys())
    removed_keys = list(data1.keys() - data2.keys())
    common_keys = list(data1.keys() & data2.keys())

    diffs.update(_process_keys(added_keys, data2, ADDED))
    diffs.update(_process_keys(removed_keys, data1, REMOVED))

    for key in common_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, Dict) and isinstance(value2, Dict):
            diffs[key] = {
                "status": NESTED,
                "diff": _generate_diffs(value1, value2),
            }
        elif value1 == value2:
            diffs[key] = {
                "status": UNCHANGED,
                "diff": value1,
            }
        else:
            diffs[key] = {
                "status": CHANGED,
                "diff": {
                    "old_value": value1,
                    "new_value": value2,
                },
            }

    return OrderedDict(sorted(diffs.items()))


def _parse_file(file_path: str):
    fmt = file_path.split(".")[-1]
    data = open(file_path)
    return parse(data, fmt)


def generate_diff(file_path1: str, file_path2: str, format_="stylish") -> str:
    data1 = _parse_file(file_path1)
    data2 = _parse_file(file_path2)

    format_diffs = formatter(format_)

    diffs = _generate_diffs(data1, data2)

    return format_diffs(diffs)
