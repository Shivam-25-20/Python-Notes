# Write a Python program to display the day of the week based on a number (1–7) using if...elif...else.

n = int(input("Enter nuber : "))

if n == 1 :
    print("Sunday")
elif n == 2 :
    print("Monday")
elif n == 3 :
    print("Tuesday")
elif n == 4 :
    print("Wednesday")
elif n == 5 :
    print("Thusday")
elif n == 6 :
    print("Friday")
elif n == 7 :
    print("Satarday")
else:
    print("Enter in range 1 to 7.")