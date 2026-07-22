import json
from pathlib import Path

DATA_PATH = Path("data") / "test_suite.json"

def load_test_suite():

    with open(DATA_PATH, "r", encoding="utf-8") as file:

        return json.load(file)