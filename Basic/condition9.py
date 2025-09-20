#Combine value

day = 7
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Now it's working days")
    case 6 | 7:
        print("I Love weekends!")
    case _:
        print("Invalid! Day")