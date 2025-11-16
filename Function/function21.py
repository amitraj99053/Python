# To specify that a function can have only keyword arguments, add  *,  before the arguments

def my_function(*, name):
    print("Hello", name)
    print("Welcome to Python functions!")
    
my_function(name = "Amit")  