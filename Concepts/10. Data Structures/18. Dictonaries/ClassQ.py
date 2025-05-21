dict1={}
n=int(input("Enter how many Students are in Your Class: "))
subjects=["Python","DBMS","OS","TOC","OAT","Discrete Structures","Sampling Theory"]
for i in range(2,n):
    print("Enter the Details for Student 1: \n")
    name=input("Enter Your Name: ")
    cgpa=float(input("Enter Your CGPA: "))
    EnRoll=input("Enter Your Enrollment Number: ")
    email=input("Enter Your Email: \n")
    dict1.update({i+2:[name,cgpa,EnRoll,email,subjects]})
print(dict1)