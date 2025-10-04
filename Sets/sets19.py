# Join set1 and set2, but keep only the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "Microsoft", "apple"}

set3 = set1.intersection(set2)
set4 = set1 & set2  # This also returns the intersection of two sets
print(set3)
print(set4)
