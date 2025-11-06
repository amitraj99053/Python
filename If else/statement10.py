# Valid user input check

username = input("Enter your username: ")

if len(username) > 0:
    print(f"Welcome, {username} to my website!")
else:
    print("Error: Username not found.")