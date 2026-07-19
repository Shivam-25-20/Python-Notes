num = (1,2,3,4,0,5,6)

for i in num:
    print(i)
for i in num:
    print(i,end=",")
print()

sum = 0

for i in num:
    sum += i
print(sum)



# range

for i in range(len(num)-1,-1,-1):
    print(num[i])