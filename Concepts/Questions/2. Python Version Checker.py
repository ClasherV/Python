"""
Question:

Write a Python program to find out what version of Python you are using.
"""

# Program:
import sys
print(f"Python Version: {sys.version}")
print()
print(f"Python Version Info: {sys.version_info}")

"""
O/p: Python Version: 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]
     
     Python Version Info: sys.version_info(major=3, minor=13, micro=1, releaselevel='final', serial=0)
"""