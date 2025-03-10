s = "Hello123"
print(s.isalpha())   # False (Contains numbers)
print(s.isdigit())   # False (Contains letters)
print(s.isalnum())   # True  (Contains only letters & numbers)
print("  ".isspace())  # True (Contains only spaces)
print("Hello".islower())  # False (Not all lowercase)
print("hello".islower())  # True
print("HELLO".isupper())  # True
print("Hello World".istitle())  # True (Each word starts with uppercase)
