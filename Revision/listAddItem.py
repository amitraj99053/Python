# To add an item to the end of the list, use the append() method

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist) 
print()

mylist.insert(1, "orange")
print(mylist)
print()

# Add the elements of "newlist" to "mylist" to extend
newlist = ["mango", "pineapple", "papaya"]
mylist.extend(newlist)
print(mylist)
print()

# Add elements of a tuple to a list
mytuple = ("kiwi", "orange")
mylist.extend(mytuple)
print(mylist)