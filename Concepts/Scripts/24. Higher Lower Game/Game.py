import random
import os
import UI
import DB
score=0
print(UI.Logo)
def displayAccountInfo(account):
    name=account['name']
    description=account['description']
    city=account['city']
    return f"{name}, a {description}, from {city}"
def checkAnswer(guess,subscriber_1,subscriber_2):
    if subscriber_1<subscriber_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_2=random.choice(DB.data)
flag=True
while flag:
    account_1=account_2
    account_2=random.choice(DB.data)
    while account_1==account_2:
        account_2=random.choice(DB.data)
    print(f"Compare 1: {displayAccountInfo(account_1)}")
    print(UI.vs)
    print(f"Compare 2: {displayAccountInfo(account_2)}")
    guess=int(input("Who has more Subscribers? Type 1 or 2: "))
    subscribers_count_1=account_1['subscribers']
    subscribers_count_2=account_2['subscribers']
    is_correct=checkAnswer(guess,subscribers_count_1,subscribers_count_2)
    os.system('cls')
    print(UI.Logo)
    if is_correct:
        score+=1
        print(f"You are Right. Your Score is: {score}")
    else:
        print(f"You are Wrong. Your Final Score is: {score}")
        flag=False