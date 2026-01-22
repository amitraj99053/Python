# Packing a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
print()


# Unpacking a tuple
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print()


# Assign the rest of the values as a list called "red" using Asterisk*
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)
print()


# Add a list of values the "tropic" variable
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits3

print(green)
print(tropic)
print(red)
