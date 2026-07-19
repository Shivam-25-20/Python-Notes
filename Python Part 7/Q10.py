# 10. Write a program to merge two lists and display the combined list.

mylist1 = [1,2,3,4,5]
mylist2 = [6,7,8,9,10]

print(mylist1+mylist2)

mylist1.extend(mylist2)
print(mylist1)