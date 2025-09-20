# AND Opr
x = 6   #  0110
y = 3   #  0011

print(6 & 3)  
"""
 6 = 0110
 3 = 0011
 2 = 0010
""" 

# OR

print(x | y)

"""
 6 = 0110
 3 = 0011
 7 = 0111
"""

# NOT

print(~x)
"""
 6 = 0110
-7 = 1001
"""

# XOR
print(x ^ y)
"""
 6 = 0110
 3 = 0011
 5 = 0101
"""

# Left shift
print(3 << 2) #  2 times
"""
 3 = 0011
12 = 1100
"""

# Right shift
print(8 >> 1)  # 1 times
"""
 8 = 1000
 4 = 0100
"""