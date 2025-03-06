import math
import os
print("This is a Basic Calculator")
print("Operations You can Perform are Addition(+), Subtraction(-), Multiplication(*), Division(/), Power(**), Remainder(%), Square(x^2), Cube(x^3), Trigonometric Functions, Rounding Figures")
another=""
sentinel=False
while not sentinel:
    print()
    print("Select an Operation: \n")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Power(**)")
    print("6. Remainder(%)")
    print("7. Square(Sq)")
    print("8. Cube(Cb)")
    print("9. Trigonometric Functions(TF)")
    print("10. Rounding Figures(RF)")
    operator=input("\nEnter the Symbol for choosing an Operation: ")
    match(operator):
        case '+': 
            addrep=False
            while not addrep:
                if another=='yes':
                    print(f"Number 1 is: {result}")
                    operand_1=result
                else:
                    operand_1=float(input("Enter the Number 1: "))
                operand_2=float(input("Enter the Number 2: "))
                if (round(operand_1,0)==operand_1) and (round(operand_2,0)==operand_2):
                    operand_1=int(operand_1)
                    operand_2=int(operand_2)
                result=operand_1+operand_2
                print(f"{operand_1} + {operand_2} = {result}\n")
                another=input("Wanna do another Operation on it? ('Yes or 'No'): ").lower()
                if another=='yes':
                    addrep=True
                elif another=='no':
                    new=input("Wanna do a New Calculation? ('Yes' or 'No'): ").lower()
                    if new=='yes':
                        clear=input("Do You want to Clear the Screen? ('Yes' or 'No'): ")
                        if clear=='yes':
                            os.system('cls')
                        another=""
                        addrep=True
                    else:
                        sentinel=True
                        addrep=True
        case '-': 
            subrep=False
            while not subrep:
                if another=='yes':
                    print(f"Number 1 is: {result}")
                    operand_1=result
                else:
                    operand_1=float(input("Enter the Number 1: "))
                operand_2=float(input("Enter the Number 2: "))
                if (round(operand_1,0)==operand_1) and (round(operand_2,0)==operand_2):
                    operand_1=int(operand_1)
                    operand_2=int(operand_2)
                result=operand_1-operand_2
                print(f"{operand_1} - {operand_2} = {result}\n")
                another=input("Wanna do another Operation on it? ('Yes or 'No'): ").lower()
                if another=='yes':
                    subrep=True
                elif another=='no':
                    new=input("Wanna do a New Calculation? ('Yes' or 'No'): ").lower()
                    if new=='yes':
                        clear=input("Do You want to Clear the Screen? ('Yes' or 'No'): ")
                        if clear=='yes':
                            os.system('cls')
                        another='no'
                        subrep=True
                    else:
                        sentinel=True
                        subrep=True
print("End of Program")