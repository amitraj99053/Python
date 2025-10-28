# Bitwise operator are used to compaire binary numbers. 

a = 6           # 6 = 0110
b = 3           # 3 = 0011

print("a & b =", a & b)   # AND Operator:  0110 & 0011 = 0010 = 2
print("a | b =", a | b)   # OR Operator:   0110 | 0011 = 0111 = 7
print("a ^ b =", a ^ b)   # XOR Operator:  0110 ^ 0011 = 0101 = 5
print("~a =", ~a)         # NOT Operator:  ~0110 = 1001 = -7
print("a << 1 =", a << 1) # Left Shift:    0110 << 1 = 1100 = 12
print("a >> 1 =", a >> 1) # Right Shift:   0110 >> 1 = 0011 = 3         
print("b << 2 =", b << 2) # Left Shift:    0011 << 2 = 1100 = 12
print("b >> 1 =", b >> 1) # Right Shift:   0011 >> 1 = 0001 = 1
print()

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~6)