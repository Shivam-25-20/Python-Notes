# Write a function that calculates the factorial of a number using recursion.


def factorial(n):
    if n >=1 :
        if n==1 :
            return 1
        else :
            return n*factorial(n-1)
    else:
        return "write positive number only."


print(factorial(-5))