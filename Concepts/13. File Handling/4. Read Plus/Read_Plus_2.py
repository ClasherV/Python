f2=open("File_2.txt","r+")
print(f2.tell())
f2.write("\nI Love My Family")
print(f2.tell())
f2.seek(0)
print(f2.tell())
print(f2.read())
f2.close()

"""
O/p: 0
     18
     0
     
     I Love My Family
"""