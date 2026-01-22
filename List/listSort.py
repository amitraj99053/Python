# Sort the list alphabetically
firstList = ["orange", "mango", "kiwi", "pineapple", "banana"]
firstList.sort()
print(firstList)
print()


# Sort the list numerically
secondList = [100, 50, 65, 82, 23]
secondList.sort()
print(secondList)
print()


# Sort the list descending
firstList.sort(reverse= True)
print(firstList)
print()


# Sort the list descending
secondList.sort(reverse= True)
print(secondList)
print()


# ----------   Customize Sort Function    ----------------
# Sort the list based on how close the number is to 50

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print()


# By default the sort() method is "case sensitive", resulting in all capital letters being sorted before lower case letters
newList = ["banana", "Orange", "Kiwi", "cherry"]
newList.sort()
print(newList)
print()


# Perform a case-insensitive sort of the list
newList.sort(key = str.lower)
print(newList)
print()


# Reverse the order of the list items
newList.reverse()
print(newList)