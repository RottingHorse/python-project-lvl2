import json
from typing import Dict


def format_diff_json(diff_dict: Dict) -> str:
    return json.dumps(diff_dict)
