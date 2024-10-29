import random
rock='✊'
paper='📃'
scissor='✂️'
img=[rock,paper,scissor]
YChoice=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: "))
if YChoice>2 or YChoice<0:
    print("\nInvalid Number")
else: 
    print(f"\nYour Choice {img[YChoice]}")
    CChoice=random.randint(0,2)
    print(f"Computer's Choice is {img[CChoice]}\n")
    if YChoice==CChoice:
        print("Draw")
    elif YChoice==2 and CChoice==0:
        print("You Lose")
    elif YChoice==0 and CChoice==2:
        print("You Win")
    elif YChoice>CChoice:
        print("You Win")
    elif YChoice<CChoice:
        print("You Lose")