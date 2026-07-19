# 10. Write a program to create a nested tuple of student records and display each student's name and marks.

info = (
    ("alice",20,"CSE"),
    ("sam",19,"mec"),
    ("ram",21,"CSE")
)

for i in info :
    print("Name : " , i[0])
    print("Age :  " , i[1])
    print("Dept : " , i[2])
    print()