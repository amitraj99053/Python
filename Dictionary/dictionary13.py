# Copy a dicttionary

original_dict = {
    'name': 'Alice',
    'age': 30,  
    'city': 'New York'
}

my_copied_dict = original_dict.copy()
print("Copy Dictionary: ", my_copied_dict)
print()  # space

my_copied_dict2 = dict(original_dict)
print("Copy Dictionary : ", my_copied_dict2)