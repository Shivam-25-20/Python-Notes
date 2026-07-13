# Write a Python program to check whether a year is a leap year.

y = int(input("enter year: "))
if y % 4 == 0:
    print("leap year")
else:
    print("not leap year")