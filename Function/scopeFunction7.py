# If you use the nonlocal keyword, the variable will belong to the outer function

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "John"
    myfunc2()
    return x

print(myfunc1())  
