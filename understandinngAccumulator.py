# program to understand accumulator pattern in lists and strings

nums = [3,5,8]
accum = []
for w in nums:
     x = w**2
     accum.append(x)
print(accum)
s = "dog"
ac = ""
for c in s:
    ac = ac + c +'-'
    print(ac)

print(ac)