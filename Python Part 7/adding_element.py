# append
mylist1 = [1, 2, 3, 4, 5]
mylist1.append(6)
mylist1.append([7,8,9])
# mylist1.append(10,11,12)  #add one element at a time.

print(mylist1)


# insert

mylist2 = ["a","b","c","d"]
#  add at  specific index
mylist2.insert(1,"e")
# mylist2.insert(-1,"e")
# mylist2.insert(4,"e")
# mylist2.insert(5,"e")
print(mylist2)

# extend

mylist3 = [10,20,30,40]

mylist3.extend([50,60])
mylist3.extend((70,80))
mylist3.extend({90,100})
mylist3.extend("12")




print(mylist3)