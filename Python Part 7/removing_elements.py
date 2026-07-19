# remove
mylist1= [1,2,3,4,4,5,6]

mylist1.remove(4)
# mylist1.remove(7)  

print(mylist1)

# pop

mylist2 = ["a","b","c","d","e"]

mylist2.pop(2)
mylist2.pop()

# mylist2.pop(5)
print(mylist2.pop(0))
print(mylist2)


#  del

mylist3 = [10,20,30,40,50]

del mylist3[3]
print(mylist3)

del mylist3[:2]
print(mylist3)

del mylist3[:]
print(mylist3)
# del mylist3
# print(mylist3)

#  clear

mylist4 = [11,22,33,44,55]
mylist4.clear()
print(mylist4)