# mylist = []

# for i in range(1,101):
#     mylist.append(i)
mylist = [i for i in range(1,101)]
print(mylist)
mylist1 = [i*i for i in range(1,101)]
print(mylist1)


even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)


result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]

print(result)