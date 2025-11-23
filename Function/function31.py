def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
        
my_function("Amit123", age = 25, city = "New York", hobby = "coding")