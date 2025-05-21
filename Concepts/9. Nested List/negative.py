names=['Vaibhav','Sahil','Sanjana']
length=len(names)
nindex=int(input("Enter the Negative Index: "))
if nindex>-length:
    print(names[nindex])
elif nindex<=-length:
    print(names[-length])