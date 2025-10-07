# Returns a new frozenset containing the union of two sets
# union()
a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7, 8})
print(a.union(b))
print(a | b)
