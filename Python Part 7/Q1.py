# 1. Write a program to create a list of five integers and print it.


mylist = [1,2,3,4,5]

print(mylist)
print("-------------------")

for i in mylist:
    print(i)

print("-------------------")

for i in mylist:
    print(i,end=",")
print()

print("-------------------")
mylist1 = [i for i in range(1,6)]

print(mylist1)