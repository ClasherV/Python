import numpy as np
import statistics as stats
baked_food=[200,150,150,130,200,220,170,188]
a=np.array(baked_food)
print(np.mean(a))
print(np.median(a))
print(stats.mode(a))
print(np.std(a))
print(np.var(a))

"""
O/p: 176.0
     179.0
     200
     29.017236257093817
     842.0
"""