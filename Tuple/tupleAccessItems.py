# Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print()


# Print the last item of the tuple
print(thistuple[-1])
print()


# Return the third, fourth, and fifth item
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[2:5])
print()


# This example returns the items from the beginning to, but NOT included, "kiwi"
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[:4])
print()


# This example returns the items from "cherry" and to the end
print(thistuple1[2:])
print()


# This example returns the items from index -4 (included) to index -1 (excluded)
print(thistuple1[-4:-1])
print()


# Check if "apple" is present in the tuple
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")