# Write a Program to Calculate the Love between You and your Partner

name1=input("What is Your Name? : ")
name2=input("What is his/her Name? : ")

name=name1+name2
name=name.lower()

t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true=t+r+u+e

l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"Your Love Score is {love_score}% and You together are like Coke and Mentos")
elif love_score>=40 or love_score<=50:
    print(f"Your Love Score is {love_score}% and You are alright together")
else:
    print(f"Your Love Score is {love_score}%")

"""
O/p 1: What is Your Name? : Vaibhav Raikwar
       What is his/her Name? : Anjali Raja
       Your Love Score is 33% and You are alright together
"""