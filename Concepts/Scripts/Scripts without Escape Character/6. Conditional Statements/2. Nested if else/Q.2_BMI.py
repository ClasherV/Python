# Write a Program to Calculate the BMI and show the Condition

weight=int(input("Enter your Weight (in kgs): "))
height_feet=int(input("Enter Your Height (feet part): "))
height_inch=float(input("Enter Your Height (inch part): "))
height_metre=(height_feet*12+height_inch)*0.0254
BMI=round(weight/height_metre**2)
if(BMI<16.0):
    print(f"Your BMI is {BMI} and You are Underweight (Severe Thinness)")
elif(BMI>16.0 and BMI<16.9):
    print(f"Your BMI is {BMI} and You are Underweight (Moderate Thinness)")
elif(BMI>17.0 and BMI<18.4):
    print(f"Your BMI is {BMI} and You are Underweight (Mild Thinness)")
elif(BMI>18.5 and BMI<24.9):
    print(f"Your BMI is {BMI} and You are under Normal Range")
elif(BMI>25.0 and BMI<29.9):
    print(f"Your BMI is {BMI} and You are Overweight (Pre-Obese)")
elif(BMI>30.0 and BMI<34.9):
    print(f"Your BMI is {BMI} and You are Obese (Class I)")
elif(BMI>35.0 and BMI<39.9):
    print(f"Your BMI is {BMI} and You are Obese (Class II)")
elif(BMI>45.0):
    print(f"Your BMI is {BMI} and You are Obese (Class III)")
else:
    print("You are a different Human Specie")

"""
O/p : Enter your Weight (in kgs): 53
      Enter Your Height (feet part): 5
      Enter Your Height (inch part): 5
      Your BMI is 19 and You are under Normal Range
"""