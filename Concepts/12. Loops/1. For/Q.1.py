# Objective: Write a Program to Calculate the Average Height from the List of Heights

# Constraints: (i) Functions that can't be used: sum(),len(), for loop should be used to mimic them
#              (ii) List can't be created manually, Input Function should be used for Input
#              (iii) Heights should be rounded off

# Hints: (i) Use Split()
#        (ii) Use Range()
#        (iii) Use Round()

# Heights=input("Enter the Heights (In cms and separated by ,): ")
# Heights_List=Heights.split(",")
# Sum,Length=0,0
# for i in Heights_List:
#     Sum+=int(i)
#     Length+=1
# Average_Height=round(Sum/Length,2)
# print(Average_Height)

# Heights=input("Enter the Heights (In cms and separated by ,): ")
# Heights_List=Heights.split(",")
# Sum,Length=0,0
# for i in Heights_List:
#     Length+=1
# for i in range(Length):
#     Heights_List[i]=int(Heights_List[i])
#     Sum+=Heights_List[i]
# Average_Height=round(Sum/Length,2)
# print(Average_Height)

# Heights=input("Enter the Heights (In cms and separated by ,): ")
# Heights_List=Heights.split(",")
# Sum,Length=0,0
# for i in Heights_List:
#     Sum+=int(i)
#     Length+=1
# else:
#     print(round(Sum/Length,2))