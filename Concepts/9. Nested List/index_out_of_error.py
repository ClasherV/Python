names=['Vaibhav','Sahil','Sanjana']
length=len(names)
index=int(input("Enter the Index: "))
if index<length-1:
    print(names[index])
elif index>=length-1:
    print(names[length-1])