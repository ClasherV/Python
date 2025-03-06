import os
folders=os.listdir("data")
print(folders)
for i in folders:
    print(os.listdir(f"data/{i}"))

"""
O/p: ['Directory 1', 'Directory 10', 'Directory 2', 'Directory 3', 'Directory 4', 'Directory 5', 'Directory 6', 'Directory 7', 'Directory 8', 'Directory 9']
     []
     []
     []
     []
     []
     []
     []
     []
     []
     []
"""