# Join Multiple sets with the union method and the | operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"Amit", "Sumit", "Rohit"}
set4 = {"apple", "banana", "cherry"}

myset1 = set1.union(set2, set3, set4)
myset2 = set1 | set2 | set3 | set4 # Another way to do the same
print(myset1)
print(myset2)