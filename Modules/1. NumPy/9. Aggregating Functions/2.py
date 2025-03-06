import numpy as np
a=[100,150,199,200,250,130]
b=[10,50,30,40,30,10]
price=np.array(a)
quantity=np.array(b)
print(f"Price: {price}\nQuantity: {quantity}\n")
print(f"Sum: {np.sum(price)}\n")
print(f"Cumulative Sum: {np.cumsum([price,quantity])}\n")
print(f"Cumulative Product (Axis=0): {np.cumprod([price,quantity],axis=0)}\n")
print(f"Cumulative Product (Axis=1): {np.cumprod([price,quantity],axis=1)}\n")

"""
O/p: Price: [100 150 199 200 250 130]
     Quantity: [10 50 30 40 30 10]
     
     Sum: 1029
     
     Cumulative Sum: [ 100  250  449  649  899 1029 1039 1089 1119 1159 1189 1199]
     
     Cumulative Product (Axis=0): [[ 100  150  199  200  250  130]
      [1000 7500 5970 8000 7500 1300]]
     
     Cumulative Product (Axis=1): [[           100          15000        2985000      597000000
         149250000000 19402500000000]
      [            10            500          15000         600000
             18000000      180000000]]
       
"""