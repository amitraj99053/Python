# Create three dictionaries, then create one dictionary that will contain the other three dictionaries

child1 = {
    "name": "Amit",
    "year": 2003
}

child2 = {
    "name": "Sachin",
    "year": 2005
}

child3 = {
    "name": "Gudiya",
    "year": 2008
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myFamily)
print()

print(myFamily["child2"])
print()

print(myFamily["child3"]["name"])