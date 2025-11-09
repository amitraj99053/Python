# Test if a is greater than b, AND if c is greater than a

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")
    print()

if a > b or a > c:
    print("At least one of the conditions is True")
    print()
    
if not a > b:
    print("a is Not graeter than b")
    