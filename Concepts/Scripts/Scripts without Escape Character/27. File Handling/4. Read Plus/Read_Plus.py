f1=open("File_1.txt","r+")
print(f1.tell())
print(f1.read())
print(f1.tell())
f1.write("\nI Love My Family")
print(f1.tell())
f1.seek(0)
print(f1.read())
f1.close()

"""
O/p: 0
     I Love My YouTube Channel
     25
     43
     I Love My YouTube Channel
     I Love My Family
"""