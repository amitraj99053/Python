day = int(input("Enter a day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("It's a weekday.")    
    case 6 | 7:
        print("It's the weekend.")
    case _:
        print("Invalid day number")
        