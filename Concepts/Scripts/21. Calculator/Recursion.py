import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number_1=float(input("Enter the Number 1: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        operation_symbol=input("Pick an Operation: ")
        number_2=float(input("Enter the Number 2: "))
        calculator_function=operations_dict[operation_symbol]
        output=calculator_function(number_1,number_2)
        print(f"{number_1} {operation_symbol} {number_2} = {output}")
        should_continue=input("Enter 'y' to Continue with {output} or 'n' to Exit").lower()
        if should_continue=='y':
            number_1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        elif should_continue=='x':
            continue_flag=False
            print("Bye")
calculator()