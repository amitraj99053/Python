# Print all values in the dictionary, one by one

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

for x in thisdict.values():
    print(x)    
    
    
print()   # space
    
for x in thisdict:
    print(thisdict[x])
    
print() # space

for x in thisdict.keys():
    print(x)
    
print() # space

for x, y in thisdict.items():
    print(x, y)