# Write a function that takes a number as an argument and prints its square.

# method 1
def square1(n):
    print("Square of",n,"is",n*n)
n= int(input("Enter number : "))
square1(n)

# method 2
square2 = lambda n : print("Square of",n,"is",n*n)

square2(n)