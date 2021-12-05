import json
import yaml


def parse_file(path: str):
    filetype = path.split('.')[-1]
    file_content = None
    if filetype in ('yml', 'yaml'):
        file_content = yaml.safe_load(open(path))
    elif filetype == 'json':
        file_content = json.load(open(path))

    for key, value in file_content.items():
        if isinstance(value, bool):
            file_content[key] = str(value).lower()
    return file_content
