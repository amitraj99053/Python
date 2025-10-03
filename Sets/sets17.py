# Join a set with a tuple
set1 = {"a", "b", "c"}
set2 = (1, 2, 3)

set3 = set1.union(set2)
# set4 = set1 | set2  
print(set3)
# The | operator does not work with tuples