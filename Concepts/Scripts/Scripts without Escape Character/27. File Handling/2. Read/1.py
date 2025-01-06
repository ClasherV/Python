with open("File_3.txt","w") as f:
    f.write("Hello World to Everybody here")
    f.truncate(10)
with open("File_3.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read(5))

"""
O/p: Hello Worl
     Hello
"""