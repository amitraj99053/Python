# Try returning the name from a decorated function and you will not get the same result

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Have a great day!"

print(myfunction.__name__) 
