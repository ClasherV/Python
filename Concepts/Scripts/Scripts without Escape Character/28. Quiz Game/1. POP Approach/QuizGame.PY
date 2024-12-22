print("*********************************************************************")
print("\nMinecraft Quiz\n")
question_bank=[
    {
        "text":"Which is the most Fragile Block among the following: ","ans":"A"
    },
    {
        "text":"Which is the Rarest Biome in Overworld: ","ans":"C"
    },
    {
        "text":"Which is the most Dangerous Mob among the following: ","ans":"B"
    },
    {
        "text":"Who is the Boss of End Dimension: ","ans":"A"
    },
    {
        "text":"Who lies under the Floor of Ancient City: ","ans":"D"
    }
]
options=[
    [
        "(A) Glass","(B) Bedrock","(C) Dirt","(D) Cobblestone"
    ],
    [
        "(A) Jungle","(B) Badlands","(C) Mushroom","(D) Taiga"
    ],
    [
        "(A) Zombie","(B) Baby Zombie","(C) Skeleton","(D) Spider"
    ],
    [
        "(A) Ender Dragon","(B) Enderman","(C) Shulker","(D) Ghast"
    ],
    [
        "(A) Creeper","(B) Blaze","(C) Wither","(D) Warden"
    ]
]
score=0
def check_ans(guess,ans):
    if guess==ans:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("*********************************************************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(f"\n{i}")
    guess=input("\nEnter Your Answer (A/B/C/D): ").upper()
    is_correct=check_ans(guess,question_bank[question_num]["ans"])
    if is_correct:
        score+=1
        print("Your Answer is Correct")
    else:
        print("Your Answer is Incorrect")
        print(f"Correct Answer is {question_bank[question_num]["ans"]}")
    print(f"Your Correct Score is: {score}/{question_num+1}")
print("*********************************************************************")
print(f"\nYou have given total of {score} Correct Answers")
print(f"Your Final Score is: {(score/len(question_bank))*100}%")

"""
O/p: *********************************************************************
     
     Minecraft Quiz
     
     *********************************************************************
     Which is the most Fragile Block among the following:
     
     (A) Glass
     
     (B) Bedrock
     
     (C) Dirt
     
     (D) Cobblestone
     
     Enter Your Answer (A/B/C/D): a
     Your Answer is Correct
     Your Correct Score is: 1/1
     *********************************************************************
     Which is the Rarest Biome in Overworld:
     
     (A) Jungle
     
     (B) Badlands
     
     (C) Mushroom
     
     (D) Taiga
     
     Enter Your Answer (A/B/C/D): b
     Your Answer is Incorrect
     Correct Answer is C
     Your Correct Score is: 1/2
     *********************************************************************
     Which is the most Dangerous Mob among the following:
     
     (A) Zombie
     
     (B) Baby Zombie
     
     (C) Skeleton
     
     (D) Spider
     
     Enter Your Answer (A/B/C/D): b
     Your Answer is Correct
     Your Correct Score is: 2/3
     *********************************************************************
     Who is the Boss of End Dimension:
     
     (A) Ender Dragon
     
     (B) Enderman
     
     (C) Shulker
     
     (D) Ghast
     
     Enter Your Answer (A/B/C/D): a
     Your Answer is Correct
     Your Correct Score is: 3/4
     *********************************************************************
     Who lies under the Floor of Ancient City:
     
     (A) Creeper
     
     (B) Blaze
     
     (C) Wither
     
     (D) Warden
     
     Enter Your Answer (A/B/C/D): d
     Your Answer is Correct
     Your Correct Score is: 4/5
     *********************************************************************
     
     You have given total of 4 Correct Answers
     Your Final Score is: 80.0%
"""