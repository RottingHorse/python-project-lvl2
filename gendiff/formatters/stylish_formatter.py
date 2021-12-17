from typing import Dict

from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED

INDENT = "    "


def _normalize_value(value, depth: int) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, Dict):
        strings = ["{"]
        whitespaces = INDENT * depth
        for k, v in value.items():
            if isinstance(v, Dict):
                strings.append(
                    "{0}{1}{2}: {3}".format(whitespaces, INDENT, k,
                                            _normalize_value(v, depth + 1))
                )
            else:
                strings.append(
                    f"{whitespaces}{INDENT}{k}: {_normalize_value(v, depth)}")
        strings.append(f"{whitespaces}}}")
        return "\n".join(strings)
    return str(value)


def _format_diff(diff_dict: Dict, depth: int) -> str:
    strings = []
    whitespaces = INDENT * depth

    for key, diffs in sorted(diff_dict.items()):
        status = diffs.get("status")
        diff = diffs.get("diff")
        if status == NESTED:
            strings.extend(
                [
                    "{0}{1}{2}: {{\n{3}".format(whitespaces,
                                                INDENT, key,
                                                _format_diff(diff, depth + 1)),
                    f"{whitespaces}{INDENT}}}"])
        elif status == CHANGED:
            old_value = diff.get("old_value")
            new_value = diff.get("new_value")
            strings.extend([
                "{0}{1}{2}: {3}".format(whitespaces, REMOVED, key,
                                        _normalize_value(old_value, depth + 1)),
                "{0}{1}{2}: {3}".format(whitespaces, ADDED, key,
                                        _normalize_value(new_value, depth + 1)),
            ])
        else:
            strings.append(
                "{0}{1}{2}: {3}".format(whitespaces, status, key,
                                        _normalize_value(diff, depth + 1)))
    return "\n".join(strings)


def format_diff(diff_dict: Dict) -> str:
    strings = ["{", _format_diff(diff_dict, depth=0), "}"]
    return "\n".join(strings)
