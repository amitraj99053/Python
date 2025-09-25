# Passing a List as an Argument
# if you send a List as an argument, it will still be a List when it reaches the function

def my_function(food):
    for x in food:
        print(x)
    
fruits = ["apple", "banana", "cherry"]
my_function(fruits)