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
        strings = ["{"]
        whitespaces = INDENT * depth
        tail = f"{whitespaces}}}"
        for k, v in value.items():
            if isinstance(v, Dict):
                strings.append(
                    DIFF_STRING.format(whitespaces, INDENT, k,
                                       _to_str(v, depth + 1))
                )
            else:
                strings.append(
                    DIFF_STRING.format(whitespaces, INDENT, k,
                                       _to_str(v, depth)))
        strings.append(tail)
        return "\n".join(strings)
    return str(value)


def _format(diff_dict: Dict, depth: int) -> str:
    strings = []
    whitespaces = INDENT * depth

    for key, diffs in diff_dict.items():
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            strings.extend([NESTED_STRING.format(whitespaces, INDENT, key,
                                                 _format(diff, depth + 1)),
                            f"{whitespaces}{INDENT}}}"])
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            strings.extend([
                DIFF_STRING.format(whitespaces, REMOVED, key,
                                   _to_str(old_value, depth + 1)),
                DIFF_STRING.format(whitespaces, ADDED, key,
                                   _to_str(new_value, depth + 1)),
            ])
        else:
            strings.append(
                DIFF_STRING.format(whitespaces, status, key,
                                   _to_str(diff, depth + 1)))
    return "\n".join(strings)


def format_(diff_dict: Dict) -> str:
    strings = ["{", _format(diff_dict, depth=0), "}"]
    return "\n".join(strings)
