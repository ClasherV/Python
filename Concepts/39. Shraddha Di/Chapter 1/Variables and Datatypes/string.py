a='Single Line'
b="Another Single Line"
c='Multi' \
'Line'
d='''Multi
Line'''
e="""Another Multi
Line"""
print(a)
print(b)
print(c)
print(d)
print(e)
print(type(a))

"""
O/p: Single Line
     Another Single Line
     MultiLine
     Multi
     Line
     Another Multi
     Line
     <class 'str'>
"""