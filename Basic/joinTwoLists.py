# Join Lists           Method 1    
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print()

# Append list2 into list1        Method 2  
for x in list2:
    list1.append(x)
    
print(list1)
