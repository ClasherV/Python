"""
Q.14 Program to calculate BMI (Body Mass Index) of a person.
     Body Mass Index is a simple calculation using a person's height and weight.
     The formula is BMI = kg/m2 where kg is a person's weight in kilogram and m2 is their height in metres squared.
"""

weight_in_kg=float(input("Enter the Weight in kg: "))
height_in_meter=float(input("Enter the Height in meters: "))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is:",bmi)

"""
O/p: Enter the Weight in kg: 56
     Enter the Height in meters: 1.5
     BMI is: 24.88888888888889
"""