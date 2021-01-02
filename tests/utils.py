import json


def read_json_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    if type(data) is str:
        return json.loads(data)
    return data
