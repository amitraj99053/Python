# Sort a list of tuples by the second element

students = [("Amit", 25), ("Sachin", 22), ("Ravi", 28)]
sorted_students = sorted(students, key=lambda x : x[1])
print(sorted_students)