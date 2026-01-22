# The remove() method removes the specified item

# Remove "banana"
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)
print()

# Remove the first occurrence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print()

# ----------------------------
# The pop() method removes the specified index
# Remove the second item
thislist1 = ["apple", "banana", "cherry"]
thislist1.pop(1)
print(thislist1)
print()


# Remove the last item
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop()
print(thislist2)
print()


# -----------------------------------
# Clear the list content
thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)
print()



# ------------------------------------
# The del keyword also removes the specified index
# Remove the first items
thislist3 = ["apple", "banana", "cherry"]
del thislist3[0]
print(thislist3)
print()


# Delete the entire list
thislist4 = ["apple", "banana", "cherry"]
del thislist4
print(thislist4)



