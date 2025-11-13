# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check

month = int(input("Enter month number: "))
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")