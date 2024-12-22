f1=open("Ada.jpg","rb")
f2=open("Ada2.jpg","wb")
for i in f1:
    f2.write(i)
f2.close()
f1.close()