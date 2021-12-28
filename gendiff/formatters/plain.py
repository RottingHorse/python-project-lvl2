from typing import Dict

from gendiff.constants import ADDED, CHANGED, COMPLEX, NESTED, REMOVED

DIFF_STRINGS = {
    ADDED: "Property '{n}' was added with value: {v}",
    REMOVED: "Property '{n}' was removed",
    CHANGED: "Property '{n}' was updated. From {o_v} to {n_v}",
}


def _to_str(value):
    if isinstance(value, Dict):
        return COMPLEX
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return value


def _format_plain_nested(diff_dict, parent):
    lines = []

    for key, diffs in diff_dict.items():
        prop_name = parent + f".{key}" if parent else f"{key}"
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            lines.append(_format_plain_nested(diff, prop_name))
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            lines.append(
                DIFF_STRINGS[status].format(n=prop_name, o_v=_to_str(old_value),
                                            n_v=_to_str(new_value)))
        elif status == ADDED:
            lines.append(
                DIFF_STRINGS[status].format(n=prop_name, v=_to_str(diff)))
        elif status == REMOVED:
            lines.append(DIFF_STRINGS[status].format(n=prop_name))
    return "\n".join(lines)


def format_plain(diff_dict: Dict) -> str:
    return _format_plain_nested(diff_dict, parent='')
