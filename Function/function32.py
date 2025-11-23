#  use both *args and **kwargs in the same function

def my_function(title, *args, **kwargs):
    print("Title: ", title)
    print("Positinal arguments: ", args)
    print("Keyword arguments: ", kwargs)
    
my_function("User Info", "Amit", "Sachin", age = 22, city = "New York")