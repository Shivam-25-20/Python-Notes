def fact(n):
    if n == 0 :
        return 1
    print(n)
    return n*fact(n-1)

n = int(input("Enter number : "))

print(fact(n))

# 5 x 4 x 3 x 2 x 1 x 1