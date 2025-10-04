# keep all items from set1 that are not in set2.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "Microsoft", "apple"}

set3 = set1.difference(set2)
set4 = set1 - set2  # This also returns the difference of two sets
print(set3)
print(set4)