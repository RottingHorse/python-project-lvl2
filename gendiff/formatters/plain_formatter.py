from typing import Dict

from gendiff.constants import (ADDED, REMOVED, CHANGED, NESTED, UNCHANGED,
                               COMPLEX)

options = {
    ADDED: "Property '{n}' was added with value: {v}".format,
    REMOVED: "Property '{n}' was removed".format,
    CHANGED: "Property '{n}' was updated. From {o_v} to {n_v}".format,
}


def _normalize_value(value):
    if isinstance(value, Dict):
        return COMPLEX
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return f"'{value}'"


def _format_diff_plain(diff_dict, parent):
    strings = []

    for key, diffs in sorted(diff_dict.items()):
        prop_name = parent + f".{key}" if parent else f"{key}"
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            strings.append(_format_diff_plain(diff, prop_name))
        elif status == UNCHANGED:
            pass
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            strings.append(
                options[status](n=prop_name, o_v=_normalize_value(old_value),
                                n_v=_normalize_value(new_value)))
        elif status == ADDED:
            strings.append(
                options[status](n=prop_name, v=_normalize_value(diff)))
        else:
            strings.append(options[status](n=prop_name))
    return "\n".join(strings)


def format_diff_plain(diff_dict: Dict) -> str:
    return _format_diff_plain(diff_dict, parent='')
