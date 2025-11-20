# Accessing values from **kwargs

def my_function(**kwargs):
    print("Type:", type(kwargs))
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("City:", kwargs["city"])
    print("All data:", kwargs)
    
my_function(name="Amit", age = 22, city="New York")