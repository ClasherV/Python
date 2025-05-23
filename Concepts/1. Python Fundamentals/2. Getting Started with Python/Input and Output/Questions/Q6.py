"""
Q.6 Print the below Pattern using Print Function using sep and end:

*END1
*~*END2
*~*~*END3
*~*~*~*END4
*~*~*END5
*~*END6
*END7

"""

print("*",end="END1\n")
print("*","*",sep="~",end="END2\n")
print("*","*","*",sep="~",end="END3\n")
print("*","*","*","*",sep="~",end="END4\n")
print("*","*","*",sep="~",end="END5\n")
print("*","*",sep="~",end="END6\n")
print("*",end="END7\n")

"""
O/p: *END1
     *~*END2
     *~*~*END3
     *~*~*~*END4
     *~*~*END5
     *~*END6
     *END7
"""