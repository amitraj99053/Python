# 	Returns whether two frozensets have an intersection
# 	isdisjoint() method

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))