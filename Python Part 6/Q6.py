# 6. Write a function that accepts three numbers and returns the largest number.

def largest(a,b,c):
    if a >= b and a >= c :
        return a
    elif b >= a and b >= c :
        return b
    else :
        return c

l= largest(6,3,18)
print("Largest : ",l)