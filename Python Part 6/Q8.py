# Write a function that accepts any number of integers using *args and returns their sum.

def sum_number1(*n):
    return sum(n)

def sum_number2(*n):
    sum = 0
    for i in n :
        sum += i
    return sum


print(sum_number1(1,2,3,4,5,6,7))
print(sum_number2(1,2,3,4,5))
print(sum_number2(1,2,3,4,5))