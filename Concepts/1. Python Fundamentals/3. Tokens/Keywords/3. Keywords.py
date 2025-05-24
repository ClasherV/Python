import keyword
print("Keyword List:",keyword.kwlist)
print()
print("if Keyword Check:",keyword.iskeyword("if"))
print("name Keyword Check:",keyword.iskeyword("name"))
print("print Keyword Check:",keyword.iskeyword("print"))

"""
O/p: Keyword List: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
     
     if Keyword Check: True
     name Keyword Check: False
     print Keyword Check: False
"""