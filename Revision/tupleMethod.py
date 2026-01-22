"""
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

# The count() method returns the number of times a specified value appears in the tuple.
# Return the number of times the value 5 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)

countNo5 = thistuple.count(5)
countNo7 = thistuple.count(7)
countNo1 = thistuple.count(1)

print(countNo5)
print(countNo7)
print(countNo1)
print()


# Search for the first occurrence of the value 8, and return its position
thistuple2 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)

positionOf8 = thistuple2.index(8)
positionOf1 = thistuple2.index(1)
# positionOf9 = thistuple2.index(9)

print(positionOf8)
print(positionOf1)
# print(positionOf9) # Error: x not in tuple