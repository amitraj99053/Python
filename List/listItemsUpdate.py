# To change the value of a specific item, refer to the index number

list = ["apple", "banana", "cherry", "kiwi", "mango", "melon", "orange"]

# updation
list[1] = "blackcurrant"
print(list)
print()

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
list[1:3] = ["blackcurrant", "watermelon"]
print(list)
print()


# Change the second and third value by replacing it with one value

list[1:3] = ["watermelon"]
print(list)
print()


# Insert "carrot" as the third items
list.insert(2, "carrot")
print(list)