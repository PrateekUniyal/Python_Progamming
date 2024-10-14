# program to try out some methods on list
mylist = []
mylist.append(3)
mylist.append(10)
print(mylist)
mylist.append(2) # Append method
mylist.append(7)
mylist.insert(2,11) # insert method
print(mylist)
print(mylist.count(2)) # count method
print(mylist.index(7)) # index method
mylist.reverse() # reverses the list
print(mylist)
mylist.sort() # sort method
print(mylist)
mylist.remove(10) # remove method
print(mylist)
lastitem = mylist.pop() # pop method
print(mylist)
print(lastitem)
