# Update Tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Convert tuple into a list
thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(y)
print(thistuple)

# Add tuple to a tuple
thistuple1 = ("apple", "banana", "cherry")
a = ("orange",)
thistuple1 += a
print(thistuple1)


# convert the tuple into a list, remove "apple" and convert it back into a tuple
thistuple2 = ("apple", "banana", "cherry")
b = list(thistuple2)
b.remove("apple")
thistuple2 = tuple(y)
print(thistuple2)