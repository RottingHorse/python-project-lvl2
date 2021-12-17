from typing import Dict

from gendiff.constants import NESTED, CHANGED, REMOVED, ADDED

INDENT = "    "


def _normalize_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, Dict):
        strings = ["{"]
        whitespaces = INDENT * depth
        for k, v in value.items():
            if isinstance(v, Dict):
                strings.append(f"{whitespaces}{INDENT}{k}: {_normalize_value(v, depth + 1)}")
            else:
                strings.append(f"{whitespaces}{INDENT}{k}: {_normalize_value(v, depth)}")
        strings.append(f"{whitespaces}}}")
        return "\n".join(strings)
    return value


def _format_diff(diff_dict: Dict, depth) -> str:
    strings = []
    whitespaces = INDENT * depth

    for key, diffs in sorted(diff_dict.items()):
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            strings.extend(
                [f"{whitespaces}{INDENT}{key}: {{\n{_format_diff(diff, depth + 1)}", f"{whitespaces}{INDENT}}}"])
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            strings.extend([f"{whitespaces}{REMOVED}{key}: {_normalize_value(old_value, depth + 1)}",
                            f"{whitespaces}{ADDED}{key}: {_normalize_value(new_value, depth + 1)}"])
        else:
            strings.append(f"{whitespaces}{status}{key}: {_normalize_value(diff, depth + 1)}")
    return "\n".join(strings)


def format_diff(diff_dict: Dict) -> str:
    strings = ["{", _format_diff(diff_dict, depth=0), "}"]
    return "\n".join(strings)
