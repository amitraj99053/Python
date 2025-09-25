# Positional Only Arguments
# To specify that a function can have only positional arguments, add , / after the arguments

def my_function(x, /):
    print(x)
    
my_function(3)