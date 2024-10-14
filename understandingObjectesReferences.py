# Program to understand objects and references

a = "banana"
b = "banana"
print(a is b)

a = [81,82,83]
b = [81,82,83]
print(a is  b)
print(a == b)
print(id(a))
print(id(b))

c = a[:]
print(c)
c[0] = 10
print(a)
print(b)
print(c)
