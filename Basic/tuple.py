thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

# One item tuple, remember the comma
thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple1 = ("apple")
print(type(thistuple1))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)
print(tuple4[1])  
print(tuple4[-1])   # Negative Indexing
print(tuple4[2:5])  # Range of Indexes
print(tuple4[-4:-1])  # Range of Negative Indexes


tuple4 = ("apple", "banana", "cherry")
if "apple" in tuple4:
  print("Yes, 'apple' is in the fruits tuple")