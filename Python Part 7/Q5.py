# 5. Write a program to insert an element at a specific position in a list.


mylist = [1,2,3,4,5,6]

n = int(input("Enter index : "))
m = int(input("Enter value : "))

mylist.insert(n,m)

print(mylist)