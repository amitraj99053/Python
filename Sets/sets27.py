# Returns a new frozenset with the intersection
# intersection() and & operators

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)