# List items are indexed and you can access them by referring to the index number

list = ["apple", "banana", "cherry", "date", "guava", "kiwi", "melon", "mango", "orange"]

print(list[1])
print(list[-1])
print(list[2:5])
print(list[:4])
print(list[2:])
print(list[-4:-1])
print()

if "apple" in list:
    print("Yes, 'apple' is in the fruits list")