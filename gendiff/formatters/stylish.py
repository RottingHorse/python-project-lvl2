from typing import Dict

from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED

INDENT = "    "
DIFF_STRING = "{0}{1}{2}: {3}"
NESTED_STRING = "{0}{1}{2}: {{\n{3}"


def _to_str(value, depth: int) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, Dict):
        lines = ["{"]
        whitespaces = INDENT * depth
        tail = f"{whitespaces}}}"
        for k, v in value.items():
            if isinstance(v, Dict):
                lines.append(
                    DIFF_STRING.format(whitespaces, INDENT, k,
                                       _to_str(v, depth + 1))
                )
            else:
                lines.append(
                    DIFF_STRING.format(whitespaces, INDENT, k,
                                       _to_str(v, depth)))
        lines.append(tail)
        return "\n".join(lines)
    return str(value)


def _format_nested(diff_dict: Dict, depth: int) -> str:
    lines = []
    whitespaces = INDENT * depth

    for key, diffs in diff_dict.items():
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            lines.extend([NESTED_STRING.format(whitespaces, INDENT, key,
                                               _format_nested(diff,
                                                              depth + 1)),
                          f"{whitespaces}{INDENT}}}"])
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            lines.extend([
                DIFF_STRING.format(whitespaces, REMOVED, key,
                                   _to_str(old_value, depth + 1)),
                DIFF_STRING.format(whitespaces, ADDED, key,
                                   _to_str(new_value, depth + 1)),
            ])
        else:
            lines.append(
                DIFF_STRING.format(whitespaces, status, key,
                                   _to_str(diff, depth + 1)))
    return "\n".join(lines)


def format_stylish(diff_dict: Dict) -> str:
    lines = ["{", _format_nested(diff_dict, depth=0), "}"]
    return "\n".join(lines)
