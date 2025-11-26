# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(1)
def myfunction():
    return "Hello Amit"

print(myfunction())