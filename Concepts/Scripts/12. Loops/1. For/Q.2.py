# Objective: Write a Program to find out the Maximum Number from a List of Numbers

# Constraints: (i) Max() can't be used
#              (ii) List can't be created manually, use Input() for Input

# Hints: Use Range(), Split()

# Numbers=input("Enter a List of Numbers (Separated by Spaces): ")
# Numbers_List=Numbers.split()
# Length,Max=0,0
# for i in Numbers_List:
#     Length+=1
# for i in range(Length):
#     Numbers_List[i]=int(Numbers_List[i])
#     if Numbers_List[i]>Max:
#         Max=Numbers_List[i]
# else:
#     print(f"Maximum Number from the above List is: {Max}")

# Numbers=input("Enter a List of Numbers (Separated by Spaces): ")
# Numbers_List=Numbers.split()
# Length=0
# for i in Numbers_List:
#     Length+=1
# for i in range(Length):
#     Numbers_List[i]=int(Numbers_List[i])
# Max=Numbers_List[0]
# for i in Numbers_List:
#     if i>Max:
#         Max=i
# print(f"Maximum Number from the above List is: {Max}")