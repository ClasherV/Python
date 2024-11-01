# Objective: Write a Program for Caeser Cipher Text (Encryption and Decryption)

# Hints: (i) Encryption Formula = En(x)=(x+n)%26
#        (ii) Decryption Formula = Dn(x)=(x-n)%26, in case x-n is -ve, we add 26 to it

# alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def encryption(plain_text,n):
#     cipher_text=""
#     for char in plain_text:
#         if char in alphabets:
#             x=alphabets.index(char)
#             new_index=x+n
#             En=new_index%26
#             cipher_text+=alphabets[En]
#         else:
#             cipher_text+=char
#     print(f"Encrypted Message: {cipher_text}")

# def decryption(cipher_text,n):
#     plain_text=""
#     for char in cipher_text:
#         if char in alphabets:
#             x=alphabets.index(char)
#             new_index=x-n
#             if new_index<0:
#                 new_index+=26
#             Dn=new_index%26
#             plain_text+=alphabets[Dn]
#         else:
#             cipher_text+=char
#     print(f"Decrypted Message: {plain_text}")

# def main():
#     terminate=False
#     while not terminate:
#         process=input("Enter 'encrypt' to Encrypt and 'decrypt' to Decrypt: ").lower()
#         message=input("Enter Your Message: ").lower()
#         shift_key=int(input("Enter the Number of Shifts: "))
#         if process=='encrypt':
#             encryption(plain_text=message,n=shift_key)
#         if process=='decrypt':
#             decryption(cipher_text=message,n=shift_key)
#         Continue=input("\nDo You want to Continue? ('Yes or No): ").lower()
#         print()
#         if Continue=='no':
#             terminate=True

# main()

# alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def task(message,n,process):
#     if process=='decrypt':
#         n*=-1
#     text=""
#     for char in message:
#         if char in alphabets:
#             x=alphabets.index(char)
#             new_index=x+n
#             if new_index<0:
#                 new_index+=26
#             Execution=new_index%26
#             text+=alphabets[Execution]
#         else:
#             message+=char
#     if process=='encrypt':
#         print(f"Encrypted Message: {text}")
#     if process=='decrypt':
#         print(f"Decrypted Message: {text}")

# def main():
#     terminate=False
#     while not terminate:
#         process=input("Enter 'encrypt' to Encrypt and 'decrypt' to Decrypt: ").lower()
#         message=input("Enter Your Message: ").lower()
#         shift_key=int(input("Enter the Number of Shifts: "))
#         task(message=message,n=shift_key,process=process)
#         Continue=input("\nDo You want to Continue? ('Yes or No): ").lower()
#         print()
#         if Continue=='no':
#             terminate=True

# main()