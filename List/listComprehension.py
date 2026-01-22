# Without list comprehension you will have to write a for statement with a conditional test inside

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
print()


# With list comprehension you can do all that with only one line of code
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits1 if "a" in x]
print(newlist1)
print()


# The condition is like a filter that only accepts the items that evaluate to True
# Only accept items that are not "apple"
bucket = ["apple", "banana", "cherry", "kiwi", "mango"]

newBucket = [x for x in bucket if x != "apple"]
print(newBucket)
print()


# The condition is optional and can be omitted
# With no if statement
newBucketList = [x for x in fruits]
print(newBucketList)
print()

# Iterable ----------------------------------------
# The iterable can be any iterable object, like a list, tuple, set etc
# You can use the range() function to create an iterable
newlistWithRange = [x for x in range(10)]
print(newlistWithRange)
print()


# Accept only numbers lower than 5
newRange = [x for x in range(10) if x < 5]
print(newRange)
print()


# Set the values in the new list to upper case
newUpperCaseOfFruits = [x.upper() for x in fruits]
print(newUpperCaseOfFruits)
print()


# Set all values in the new list to 'hello' 
# replacement
newValueSet = ['hello' for x in fruits]
print(newValueSet)
print()



# Return "orange" instead of "banana"
changeValue = [x if x != "banana" else "orange" for x in fruits]
print(changeValue)
