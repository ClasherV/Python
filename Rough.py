import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['@','#','$','%','&','*','(',')']
number=['0','1','2','3','4','5','6','7','8','9']
password_list=""
print("welcome to password generator!")

n_letters=int(input("How many letter do you want in the password? \n"))
n_symbol=int(input("How many  symbol do you want in the password?\n "))
n_number=int(input("How many number do you want in the password? \n"))

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
   
for i in range(1,n_symbol+1):
    char=random.choice(symbol)
    password_list+=char

for i in range(1,n_number+1):
   char=random.choice(number)
   password_list+=char
print(f"password:{password_list}")