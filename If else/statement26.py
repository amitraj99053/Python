# Grade calculation with nested logic

score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("Grade: A+")
    else:
        print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")