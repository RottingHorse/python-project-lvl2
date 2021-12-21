import json
import yaml


def parse(data, fmt):
    if fmt in ('yml', 'yaml'):
        return yaml.safe_load(data)
    elif fmt == 'json':
        return json.load(data)
