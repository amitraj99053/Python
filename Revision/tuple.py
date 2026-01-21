# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print()


# Tuples allow duplicate values
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
print()


# Print the number of items in the tuple
print(len(thistuple))
print()


# One item tuple, remember the comma
mytuple = ("apple",)
print(type(thistuple))
print(type(mytuple))
print()


# NOT a tuple
mytuple1 = ("apple")
print(type(mytuple1))
print()


# Tuple items can be of any data type
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print()


# Using the tuple() method to make a tuple
newTuple = tuple(("apple", "banana", "cherry"))
print(newTuple)
