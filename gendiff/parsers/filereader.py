from gendiff.parsers.parser import parse


def parse_file(file_path: str):
    fmt = file_path.split(".")[-1]
    data = open(file_path)

    return parse(data, fmt)
