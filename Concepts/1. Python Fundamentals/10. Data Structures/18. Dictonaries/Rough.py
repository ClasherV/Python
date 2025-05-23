dict={}
flag=False
while not flag:
    name=input("Enter Your Name: ")
    age=int(input("Enter Your Age: "))
    dict[name]=age
    sentinel=input("Do You want to Continue?: ").lower()
    if sentinel=='no':
        flag=True
print(dict)