age = int(input("Enter your age : "))
has_id = input("Enter Y or N for Id :")

if age >= 18:
    if has_id == "Y":
        print("Entry Allowed")
    elif has_id == "N" :
        print("ID requied")
    else :
        print("Write properly")
else :
    print("Entry denied")