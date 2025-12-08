# Identifying base case and recursive case

def recursive_function(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_function(n - 1)


print(recursive_function(5))
