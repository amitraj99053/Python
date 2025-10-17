# keys()
# values()
# The keys() method returns a view object that displays a list of all the keys in the dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964,
}

x = car.keys()
y = car.values()
print(x) # before the change
print(y)

car["color"] = "white"
car["year"] = 2020

print(x)  # after the change
print(y)