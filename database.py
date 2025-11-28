import json
import os

DB_FILE = "library_data.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {"books": [], "students": [], "issued": []}

    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)
