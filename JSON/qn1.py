# Convert from JSON to Python using json.loads() method

import json

# Sample JSON string
json_string = '{"name": "Amit", "age": 23, "city": "New York"}'

# Parse JSON string
parsed_json = json.loads(json_string)

# the result is a Python dictionary
print(parsed_json) 
print(type(parsed_json)) 
print(parsed_json["name"])