# Returns a new frozenset with the symmetric differences of two sets
# The symmetric difference of two sets is the set of elements that are in either of the sets
# symmetric_difference()

a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7, 8})
print(a.symmetric_difference(b))  
print(a ^ b)               
