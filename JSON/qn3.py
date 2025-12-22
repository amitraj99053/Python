# Convert Python objects into JSON strings, and print the values

import json

print(json.dumps({"name": "Amit", "age": 23, "city": "New York"}))  # dictionary
print(json.dumps(["apple", "banana", "cherry"]))    # list
print(json.dumps(("apple", "banana", "cherry")))    # tuple
print(json.dumps("hello"))                   # string
print(json.dumps(42))                     # integer
print(json.dumps(3.14))                 # float
print(json.dumps(True))                    # boolean
print(json.dumps(False))                   # boolean
print(json.dumps(None))                    # null

