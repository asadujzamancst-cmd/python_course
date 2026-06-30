import json

# Python object
person_data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# json.dumps() → Python object → JSON string
person_json_convert = json.dumps(person_data)
print(person_json_convert)

# json.loads() → JSON string → Python object
person_json = '{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}'
person = json.loads(person_json)
print(person)

# json.dump() → Python object → JSON file
with open("person_data.json", "w") as json_file:
    json.dump(person_data, json_file)

# json.load() → JSON file → Python object
with open("person_data.json", "r") as json_file:
    json_read = json.load(json_file)
    print(json_read)