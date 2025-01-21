import numpy as np
a=[100,150,199,200,250,130]
b=[10,50,30,40,30,10]
price=np.array(a)
quantity=np.array(b)
print(f"Price: {price}\nQuantity: {quantity}\n")
var=np.cumprod([price,quantity],axis=0)
print(var[1].sum())

"""
O/p: Price: [100 150 199 200 250 130]
     Quantity: [10 50 30 40 30 10]
     
     31270    
"""