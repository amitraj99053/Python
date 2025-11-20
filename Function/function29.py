# Using **kwargs to accept any number of keyword arguments

def my_function(**kid):
    print("His last name is " + kid["lname"])
    
my_function(fname="Amit", lname="Kumar")
my_function(fname="Sachin", lname="Kumar Yadav", age=7)