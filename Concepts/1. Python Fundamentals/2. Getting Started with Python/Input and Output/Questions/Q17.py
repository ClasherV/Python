"""
Q.17 Write a program to input a value in tonnes and convert it into quintals and kilograms.
     (1 tonne=10 quintals, 1 tonne=1000 kgs,1 quintal=100 kg )
"""

tonnes=float(input("Enter tonnes:"))
quintals=tonnes*10
kgs=quintals*100
print("Tonnes:",tonnes)
print("Quintals:",quintals)
print("Kilograms:",kgs)

"""
O/p: Enter tonnes:2
     Tonnes: 2.0
     Quintals: 20.0
     Kilograms: 2000.0
"""