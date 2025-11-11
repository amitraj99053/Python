# Login validation with nested checks

username = input("Enter username: ")
password = input("Enter password: ")
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is inactive")
    else:
        print("Password required")
else:
    print("Username required")