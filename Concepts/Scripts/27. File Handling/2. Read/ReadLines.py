f=open("File_2.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)

"""
O/p: Hello Friends
     
     I'll Rise Again
     
     For Sure Maa
"""