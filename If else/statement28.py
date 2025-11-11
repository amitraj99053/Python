# Using pass in different branches

value = int(input("Enter a number: "))

if value < 0:
    print("Negative value")
elif value == 0:
    pass  # No action needed for zero
else:
    print("Positive value")
    