mylist = ["apple", "banana", "carrot"]
list1 = [1, 5, 4, 7, 9]
list2 = ["apple", 34, True, 40, "male", False]
list3 = list(("apple", "banana"))

print(mylist)
print(list1)
print(list2)
print(len(mylist))   # len()
print(type(list1))   # type()
print(type(list2))
print(list3)

print()
print(list1[1])
print(list1[-1])

print(list2[2])
print(list2[2:5])
print(list2[:5])
print(list2[2:])
print(list2[-5:-2])


if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")
    
    
print() # for space only

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"  # update value
print(thislist)



thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)

newlist = ["apple", "banana", "cherry"]
newlist.insert(2,"watermelon")    # insertion
print(newlist)

newlist1 = ["apple", "banana", "cherry"]
newlist1.append("orange")        # insertion
print(newlist1)


newlist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
newlist2.extend(tropical)      # extend two list into single one
print(newlist2)


newlist3 = ["apple", "banana", "cherry"]
newlist3.remove("banana")    # remove
print(newlist3)

newlist4 = ["apple", "banana", "cherry", "banana", "kiwi"]
newlist4.remove("banana")
print(newlist4)
newlist4.clear()
print(newlist4)

# these functions are also used to remove
# pop()
# del()