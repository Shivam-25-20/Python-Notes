# Write a function that accepts student details using **kwargs and displays each key-value pair.

def student_detail(**detail):
    for key , value in detail.items():
        print(key,":",value)

student_detail(name = "Alice", age = 22 ,grade = "C")