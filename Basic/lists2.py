# List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# without list comprehension we have to use 'for' statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for y in fruits:
    if "a" in y:
        newlist.append(y)
        
print(newlist)


# With list comprehension in one line of code
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [z for z in fruits1 if "a" in z]
print(newlist1) 

# Sort the list alphabetically
fruits1.sort()


thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits2.sort(reverse = True)
print(fruits2)

thislist2 = [100, 50, 65, 82, 23]
mylist = thislist2.copy()
print(mylist)