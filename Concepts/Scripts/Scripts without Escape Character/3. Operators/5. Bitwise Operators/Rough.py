import random
Rock= '✊'
paper='📄'
scissor='✂'
game=[Rock,paper,scissor]
print("Enter 0. for ✊, 1. for  📄 and 2. for scissor ✂  ")
user_choice=int(input("Enter your choice!: "))
if(user_choice>=3 or user_choice<0):
    print("You have entered wrong choice!")
else:
    computer_choice=random.randint(0,2)
    print("Computer choose: ", game[computer_choice])
    print("user choose: ", game[user_choice])
    if(user_choice==0 and computer_choice==1 or user_choice==1 and computer_choice==2 or user_choice==2 and computer_choice==0 ):
        print("you Loose!")
    elif(user_choice==0 and computer_choice==2 or user_choice==1 and computer_choice==0 or user_choice==2 and computer_choice==1 ):
        print("you Win!")
    elif(user_choice==computer_choice):
        print("Tie")