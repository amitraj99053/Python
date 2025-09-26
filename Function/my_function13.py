# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
    
my_function(5, 6, c = 7, d = 8)