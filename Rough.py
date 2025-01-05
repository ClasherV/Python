import random

print(" Think a number from  1 to 50")
Random = random.randint(1, 50)
# print(Random)
level = input("Choose level of difficulty....Type 'easy' or 'hard':\n ").lower()


def guess_num(attempt):
    print(f"You have {attempt} attempts remaining to guess the number!\n")
    wanna_end = True
    while wanna_end:
        guess = int(input("Make a guess: "))
        attempt = attempt - 1
        if (guess > 50):
            print("Invalid guess!\n")
        if (guess <= 0):
            print("Invalid guess!\n")
        if (guess > Random and guess <= 50):
            print("Your guess is too high")
            print("Guess again!\n")
        if (guess < Random and guess > 0):
            print("Your guess is too low")
            if (attempt >= 1 and attempt <= 9):
                print("Guess again!\n")
        if (guess == Random):
            print("You won! ")
            print("Good Bye! ")
            wanna_end = False
        if (guess != Random):
            if (attempt >= 1 and attempt <= 9):
                print(f"You have {attempt} attempt remaining to guess the number")
        if (attempt == 0):
            print("You are out guesses.....")
            wanna_end = False


if (level == 'easy'):
    attempt = 10
    guess_num(attempt)
elif (level == 'hard'):
    attempt = 5
    guess_num(attempt)