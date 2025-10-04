# keep the items that are not present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "Microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
set4 = set1 ^ set2 # This also returns the symmetric difference of two sets
print(set3)
print(set4)