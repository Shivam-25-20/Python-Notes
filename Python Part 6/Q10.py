# 10. Write a function that returns both the quotient and remainder of two numbers.


def quotient_remainder(a,b):
    if b == 0 :
        print("B cannot be zero")
    else:
        print("Quotient of",a,"by",b,"is",a//b)
        print("remainder of",a,"by",b,"is",a%b)


quotient_remainder(5,8)
quotient_remainder(34,3)
quotient_remainder(34,0)
