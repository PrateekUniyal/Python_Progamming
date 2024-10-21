# program to practice split and join method in python

s = "This string is used for split and join operation."
# slist = s.split('used')
slist = s.split()
print(slist)
glue = "-"
newS = glue.join(slist)
print(newS)
glue = "*"
newS = glue.join(slist)
print(newS)

st = input("Please enter the string for performing split and join:")
print("s for split and j for join:")
choice = input()
if choice == "s":
    de = input("Please enter the delimiter: ")
    lst = st.split(de)
    print("The string after split is : ")
    print(lst)
elif choice == "j":
    glue = input("Please enter the glue: ")
    string = glue.join(st)
    print("The string after the join operation is : ")
    print(string)
else:
    print("Invalid input.")
