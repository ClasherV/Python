f3=open("File_3.txt","w+")
print(f3.tell())
print(f3.read())
print(f3.tell())
f3.write("Kaise ho sab log")
print(f3.tell())
f3.seek(0)
print(f3.read())
print(f3.tell())
f3.close()

"""
O/p: 0
     
     0
     16
     Kaise ho sab log
     16
"""