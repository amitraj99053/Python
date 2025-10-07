# Returns True if this frozenset is a (proper) subset of another frozenset
# issubset()

a = frozenset({1, 2})
b = frozenset({1, 2, 3, 4})
print(a.issubset(b))
print(a <= b)
print(a < b)
print(b.issubset(a))
print(b <= a)
print(b < a)    
