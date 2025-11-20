# finding the maximum value

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 5, 2, 8, 1))
print(my_function(-10, -5, -3, -1))
print(my_function())