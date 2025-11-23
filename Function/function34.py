# Using ** to unpack a dictionary into keyword arguments

def my_function(fname, lname):
    print("Hello", fname, lname)
    
person = {"fname": "Amit", "lname": "Kumar"}
my_function(**person)