def add(*number):
    sum = 0
    for num in number:
        sum += num
    print("The sum is:", sum)
    print(number)
    print(type(number))

add(1, 2, 3,20,673,46,45,6)