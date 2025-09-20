# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
    x = "fantastic"
print("Python is " + x)

myfunc()

print("Python is " + x)
