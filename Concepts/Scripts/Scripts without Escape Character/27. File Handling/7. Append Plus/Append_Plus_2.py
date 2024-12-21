f2=open("File_2.txt","a+")
f2.write("\nMinecraft mein")
f2.seek(0)
print(f2.read())
f2.close()

"""
O/p: Toh aaj hai ek aur suhana din
     Minecraft mein
"""