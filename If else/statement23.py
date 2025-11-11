# Three levels of nesting

score = 85
attendance = 90
submitted_assignments = True

if score >= 60:
    if attendance >= 75:
        if submitted_assignments:
            print("Pass with good standing")
        else:
            print("Pass but missing assignments")
    else:
        print("Pass but low attendence")
else:
    print("Fail")
    