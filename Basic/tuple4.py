# Python Unpack tuples

# Paking a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Unpacking a tuple
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)


# Using Asterisk *
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1
print(green)
print(yellow)
print(red)
print()
 
 
(green, *tropic, red,blue) = fruits1
print(green)
print(tropic)
print(red)
print(blue)
