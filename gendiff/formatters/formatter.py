from gendiff.formatters.json_ import format_ as json_
from gendiff.formatters.plain import format_plain as plain
from gendiff.formatters.stylish import format_stylish as stylish


def formatter(fmt: str):
    formatters = {
        "stylish": stylish,
        "plain": plain,
        "json": json_,
    }
    return formatters.get(fmt)
