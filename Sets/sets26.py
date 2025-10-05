# Return a shallow copy

fs = frozenset({1, 2, 3, 4, 5})
cp = fs.copy()
print(fs)
print(cp)
print(type(cp))
