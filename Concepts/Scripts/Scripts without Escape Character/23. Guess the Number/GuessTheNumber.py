import random
import Logo
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def setDifficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return    
def checkAnswer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print("Your guess is right. The Answer was {answer}")
def game():
    print(Logo.logo)
    print("Let me think of a Number between 1 to 50")
    answer=random.randint(1,50)
    level=input("Choose the Difficulty Level (Type 'Easy' or 'Hard'): ").lower()
    attempts=setDifficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You have chosen wrong difficulty level. Play again")
        return 
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} remaining to guess the Number")
        guessed_number=int(input("Guess a Number: "))
        attempts=checkAnswer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses. You Lose!!")
            return 
        elif guessed_number!=answer:
            print("Guess again")
game()