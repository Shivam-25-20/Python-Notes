# Write a Python program to find the larger of two numbers.

n = int(input("Enter 1st number : "))
m = int(input("Enter 2nd number : "))

if n>m:
    print(n,"is greater")
elif n<m:
    print(m,"is greater")
else:
    print("Both are equal")