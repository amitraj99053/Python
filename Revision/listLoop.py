# You can loop through the list items by using a for loop

# Print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)  
print()  #newline


# Print all items by referring to their index number
list = ["apple", "banana", "cherry"]
for i in range(len(list)):
    print(list[i])
print()


# -----------------------------------
# Print all items, using a while loop to go through all the index numbers
mylist = ["apple", "banana", "cherry"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i+1
print()


# A short hand for loop that will print all items in a list
newlist = ["apple" , "banana", "cherry"]
[print(x) for x in newlist]