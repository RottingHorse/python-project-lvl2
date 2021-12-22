from gendiff.formatters.json_ import format_ as json_
from gendiff.formatters.plain import format_ as plain
from gendiff.formatters.stylish import format_ as stylish


def formatter(fmt: str):
    formatters = {
        "stylish": stylish,
        "plain": plain,
        "json": json_,
    }
    return formatters.get(fmt)
