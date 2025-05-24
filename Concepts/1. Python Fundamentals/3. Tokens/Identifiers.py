# snake_case ----> variable_name
# camelCase ----> functionName but snake_case is recommended
# PascalCase ----> ClassName
# UPPER_SNAKE_CASE ----> CONSTANT_NAMES

print("age".isidentifier())
print("for".isidentifier())
print("1".isidentifier())
print("_".isidentifier())
print("@".isidentifier())
print("1Name".isidentifier())
print("Name1".isidentifier())

"""
O/p: True
     True
     False
     True
     False
     False
     True
"""