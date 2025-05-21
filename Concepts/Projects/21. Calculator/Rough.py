stages=["""
          +-----+
          |     |
          O     |
         /|\    |
         / \    |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|\    |
         /      |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|\    |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|     |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
          |     |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
                |
                |
                |
        ========+""",
        """
          +-----+
          |     |
                |
                |
                |
                |
        ========+"""]

import random
word_list=["apple","banana"]
lives=6
random_word=random.choice(word_list)
print(random_word)
random_space=[]
for i in range(len(random_word)):
    random_space+="_"
print(random_space)

game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ")
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter==guessed_letter:
            random_space[position]=guessed_letter
    print(random_space)
    if guessed_letter not in random_word:
        lives=lives-1
        if lives==0:
            game_over=True
            print("You lose")
    if '_' not in random_space:
        game_over=True
        print("You win!")
print(stages[lives])