import json

with open('data.json', 'r') as f:
    data = json.load(f)
    for p in data['practitioners']:
        print(f"name: {p['name_given']}")