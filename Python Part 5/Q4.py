# Write a Python program to calculate the sum of the first N natural numbers.

n = int(input("Enter number: "))
sum = 0
for i in range(n+1):
    sum += i
print(sum)