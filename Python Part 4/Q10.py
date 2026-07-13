# Write a Python program to find the largest of three numbers using nested if statements.

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if a > b :
    if a > c :
        print("1st number is largest")
    else:
        print("3rd number is largest")
else:
    if b > c :
        print("2nd number is largest")
    else:
        print("3rd number is largest")