# Nested if statements
num = 41

if num > 10:
    print("Above 10,")
    if num > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
else:
    print("Less than or equal to 10")