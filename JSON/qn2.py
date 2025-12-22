# Convert from Python to JSON using json.dumps() method

import json

# Sample Python dictionary
python_dict = {
    "name": "Amit",
    "age": 23,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_dict)

# the result is a JSON string
print(json_string)
print(type(json_string))