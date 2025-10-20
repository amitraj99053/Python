# Removing Items from a Dictionary

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'occupation': 'Engineer',
    'hobby': 'Photography'
}

my_dict.pop('age')  # Remove item with key 'age'
print(my_dict)
print()

my_dict.popitem()  # Remove the last inserted item
print(my_dict)
print()


del my_dict['city']  # Remove item with key 'city'
print(my_dict)
print()

my_dict.clear()  # Remove all items from the dictionary
print(my_dict)