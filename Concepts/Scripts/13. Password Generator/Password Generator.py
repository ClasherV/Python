# Password Generator Level 1 (Easy (No Shuffling))

# Hints: Can Use Lists, Random, Loops, Strings

# import random
# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','\\','|',';',':','\'','\"',',','.','<','>','/','?']
# print("Welcome to Password Generator")
# n_letters=int(input("Enter how much Letter You want in Your Password: "))
# n_numbers=int(input("Enter how much Numbers You want in Your Password: "))
# n_symbols=int(input("Enter how much Symbols you want in Your Password: "))
# password=""
# for i in range(n_letters):
#     password+=random.choice(letters)
# for i in range(n_numbers):
#     password+=random.choice(numbers)
# for i in range(n_symbols):
#     password+=random.choice(symbols)
# print(f"Password: {password}")

# Password Generator Level 2 (Hard Level (Shuffling))

# import random
# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','\\','|',';',':','\'','\"',',','.','<','>','/','?']
# print("Welcome to Password Generator")
# n_letters=int(input("Enter how much Letter You want in Your Password: "))
# n_numbers=int(input("Enter how much Numbers You want in Your Password: "))
# n_symbols=int(input("Enter how much Symbols you want in Your Password: "))
# password_list=[]
# for i in range(n_letters):
#     password_list+=random.choice(letters)
# for i in range(n_numbers):
#     password_list+=random.choice(numbers)
# for i in range(n_symbols):
#     password_list+=random.choice(symbols)
# random.shuffle(password_list)
# password=""
# for i in password_list:
#     password+=i
# print(f"Password: {password}")