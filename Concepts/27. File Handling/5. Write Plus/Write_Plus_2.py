f2=open("File_2.txt","w+")
print(f2.tell())
f2.write("Hey Buddies")
print(f2.tell())
f2.seek(0)
print(f2.read())
print(f2.tell())
f2.close()

"""
O/p: 0
     11
     Hey Buddies
     11
"""