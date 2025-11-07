# Setting a default value

username = ""

display_name = username if username else "Guest User"
print("Welcome,", display_name)