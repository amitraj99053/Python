# Loop through the keys and values of all nested dictionaries

myFamily = {
    "child1": {
        "name": "Amit",
        "year": 2003
    },
    
    "child2": {
        "name": "Sachin",
        "year": 2005
    }, 
    
    "child3": {
        "name": "Gudiya",
        "year": 2008
    }
}

for x, obj in myFamily.items():
    print(x)
    
    for y in obj:
        print(y , ": ", obj[y])
        
        