# Convert a Python object containing all the legal data types

import json

data = {
    "Name": "Amit Kumar",
    "Age": 22,
    "IsStudent": True,
    "IsEmployed": False,
    "Courses": None,
    "Skills": ("Python", "Java", "C++"),
    "HigherStudies": {
        "Masters": "Master of Computer Applications",
        "University": "AKTU",
        "Year": 2026
    },    
        
    "Address": [
        {"Current Address": "Gamma 1, Greater Noida", "Pin Code": 201310},
        {"Permanent Address": "Hazaribagh, Jharkhand", "Pin Code": 825301}
    ]
}

print(json.dumps(data))
print() 

# Use the indent parameter to define the numbers of indents
print(json.dumps(data, indent=4))
print()

# Use the separators parameter to change the default separator
print(json.dumps(data, indent=4, separators=(". ", " = ")))
print()

# Use the sort_keys parameter to specify if the output should be sorted or not
print(json.dumps(data, indent=4, sort_keys=True))