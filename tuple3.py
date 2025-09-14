# Update Tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# tuple into a list
thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(y)

print(thistuple)
