# Convert the tuple into a list to be able to change it
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)

print(mytuple)
print()


# Convert the tuple into a list, add "orange", and convert it back into a tuple
thisTuple = ("apple", "banana", "cherry")
myList = list(thisTuple)
myList.append("orange")
thisTuple = tuple(myList)

print(thisTuple)
print()


# Create a new tuple with the value "orange", and add that tuple
thisTuple2 = ("apple", "banana", "cherry")
myTuple = ("orange",)
thisTuple2 += myTuple

print(thisTuple2)
print()


# -----------   Remove     --------------------

# Convert the tuple into a list, remove "apple", and convert it back into a tuple
thisTuple3 = ("apple", "banana", "cherry")
myList3 = list(thisTuple3)
myList3.remove("apple")
thisTuple3 = tuple(myList3)

print(thisTuple3)
print()


# The del keyword can delete the tuple completely
thisTuple4 = ("apple", "banana", "cherry")
del thisTuple4
print(thisTuple4) # this will raise an error because the tuple no longer exists