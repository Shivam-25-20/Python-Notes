def student(**kwargs):
    print("-----------------")
    print(kwargs)
    print("Name : ",kwargs["name"])
    print(type(kwargs))                 # Dict
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Alice", age=20, city="Delhi")
student(name="Alice", age=20, city="Delhi")
student(name="Alice", age=20, city="Delhi",gender = "male",Grade = "B",marks = 78)