# Write a Program to Calculate the BMI of given Data

weight=float(input("Enter Your Weight (in kgs): "))
height_feet=int(input("\nEnter Your Height (feet part): "))
height_inch=float(input("Enter Your Height (inch part): "))
height=(height_feet*12+height_inch)*0.0254
BMI=weight/height**2
print("Your BMI is: ")
print(BMI)

"""
O/p: Enter Your Weight (in kgs): 53
     
     Enter Your Height (feet part): 5
     Enter Your Height (inch part): 5
     Your BMI is: 
     19.44382586990026
"""