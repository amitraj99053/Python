# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function
# Functions with arguments can also be decorated

def changecase(func):
    def myinner(name):
        return func(name).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

print(myfunction("Amit"))