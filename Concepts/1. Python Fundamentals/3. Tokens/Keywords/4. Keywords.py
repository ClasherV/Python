import keyword
print("Soft Keyword List:",keyword.softkwlist)
print()
print("match Soft Keyword Check:",keyword.issoftkeyword("match"))
print("_ Soft Keyword Check:",keyword.issoftkeyword("_"))
print("for Soft Keyword Check:",keyword.issoftkeyword("for"))
print("name Soft Keyword Check:",keyword.issoftkeyword("name"))

"""
O/p: Soft Keyword List: ['_', 'case', 'match', 'type']
     
     match Soft Keyword Check: True
     _ Soft Keyword Check: True
     for Soft Keyword Check: False
     name Soft Keyword Check: False
"""