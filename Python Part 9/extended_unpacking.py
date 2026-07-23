num = (1,2,3,4,5,6,7,8)

first,*middle,last = num

print(first)
print(middle)
print(last)

first,*remaning = num
print(first)

*remaning ,last = num
print(remaning)
print(last)


first , *_ , last = num

print(first)
print(last)