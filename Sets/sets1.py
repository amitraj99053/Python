# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
# Output: {'banana', 'cherry', 'apple'}

print()


# Duplicate values will be ignored
thisset1 = {"apple", "banana", "cherry", "apple"}
print(thisset1)
print()

# The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset2)

# The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset3 = {"apple", "banana", "cherry", False, True, 0}
print(thisset3)

