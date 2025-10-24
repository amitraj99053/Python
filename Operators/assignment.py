# Assignment operators are used to assign values to variables

x = z = a = b = c = d = e = f = g = h = i = j = 5         # Simple assignment
print(x)

x += 5
print(x)

z -= 5
print(z)
         
a *= 5
print(a)

b /= 5
print(b)

c %= 5
print(c)
  
d //= 5
print(d)

e **= 5
print(e)

f &= 5
print(f)

g |= 5
print(g)

h ^= 5
print(h)

i >>= 5
print(i)

j <<= 5
print(j)

print(k := 5)

print()

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")
    
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
    
    