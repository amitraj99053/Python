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

    