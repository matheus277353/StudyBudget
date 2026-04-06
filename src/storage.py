import json
import os
from typing import Dict, Any

DATA_FILE = "studybudget_data.json"

def load_data() -> Dict[str, Any]:
    """Carega os dados do arquivo JSON local."""
    if not os.path.exists(DATA_FILE):
        return {"subjects": {}}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"subjects": {}}

def save_data(data: Dict[str, Any]) -> None:
    """Salva os dados no arquivo JSON local."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
