# Iterate through the items and print the values
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()


# Use the range() and len() functions to create a suitable iterable
# Print all items by referring to their index number

myTuple = ("apple", "banana", "cherry")
for i in range(len(myTuple)):
    print(thistuple[i])
    
print()


# Print all items, using a while loop to go through all the index numbers
i = 0
while i < len(myTuple):
    print(myTuple[i])
    i = i + 1
    
