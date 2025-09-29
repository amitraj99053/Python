# Get the number of items in a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print()

# set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3, 9, 8, 2}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
print()

# A set can contain different data types
set4 = {"abc", 34, True, 40, "male"}
print(set4)
print()

# type()
print(type(set4))
print(type(set2))
print()

# The set() constructor
thisset1 = set(("apple", "banana", "cherry")) 
print(thisset1)
# Note: the set list is unordered, so the result will display the items in a random order.
