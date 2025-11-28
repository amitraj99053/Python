# Sort strings by length

words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda x : len(x))
print(sorted_words)