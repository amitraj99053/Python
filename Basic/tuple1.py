# Convert the tuple into a list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Method 2 using append()
thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(z)
print(thistuple)

# Add tuple to a tuple
thistuple1 = ("apple", "banana", "cherry")
a = ("orange",)
thistuple1 += a
print(thistuple1)


# Remove Items
thistuple2 = ("apple", "banana", "cherry")
b = list(thistuple2)
b.remove("apple")
thistuple2 = tuple(b)
print(thistuple2)


