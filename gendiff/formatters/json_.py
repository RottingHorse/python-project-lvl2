import json
from typing import Dict


def format_(diff_dict: Dict) -> str:
    return json.dumps(diff_dict)
