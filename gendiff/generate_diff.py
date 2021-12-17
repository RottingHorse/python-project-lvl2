from typing import Dict

from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED
from gendiff.formatters.stylish_formatter import format_diff
from gendiff.parser import parse_file


def _get_formatter(fmt: str):
    formatters = {
        "stylish": format_diff
    }
    return formatters.get(fmt)


def _process_added_keys(file1: Dict, file2: Dict) -> Dict:
    diffs = {}
    added_keys = list(file2.keys() - file1.keys())
    for key in added_keys:
        diffs[key] = {
            "status": ADDED,
            "diff": file2.get(key),
        }
    return diffs


def _process_removed_keys(file1: Dict, file2: Dict) -> Dict:
    diffs = {}
    added_keys = list(file1.keys() - file2.keys())
    for key in added_keys:
        diffs[key] = {
            "status": REMOVED,
            "diff": file1.get(key),
        }
    return diffs


def _check_diffs(file1: Dict, file2: Dict) -> Dict:
    diffs = {}

    diffs.update(_process_added_keys(file1, file2))
    diffs.update(_process_removed_keys(file1, file2))

    common_keys = list(file1.keys() & file2.keys())

    for key in common_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if isinstance(value1, Dict) and isinstance(value2, Dict):
            diffs[key] = {
                "status": NESTED,
                "diff": _check_diffs(value1, value2),
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

    return diffs


def generate_diff(file_path1: str, file_path2: str, formatter="stylish") -> str:
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)

    format_diffs = _get_formatter(formatter)

    diffs = _check_diffs(file1, file2)

    return format_diffs(diffs)
