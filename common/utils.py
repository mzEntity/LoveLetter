import json

def read_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    return data