import json

def load_data():
    with open('configs.json', 'r', encoding='utf-8') as file:
        return json.load(file)
