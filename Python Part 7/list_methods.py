# index

mylist = [3,4,2,4,6,11,45,67,33]

print(mylist.index(2))
print(mylist.index(4))
print(mylist.index(11))
# print(mylist.index(1))       

# count 

print(mylist.count(4))

# sort
mylist.sort()

print(mylist)
mylist.sort(reverse=True)

print(mylist)
print(mylist.sort())

# reverse

mylist.reverse()
print(mylist)


#  copy

l = mylist.copy()

print(l)