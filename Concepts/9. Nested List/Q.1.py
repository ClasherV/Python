Vault=[["*","*","*"],["*","*","*"],["*","*","*"]]
Coordinates=input("Enter where You want to Hide the Money in a 2 Digit Combination (11,12,13,21,22,23,31,32,33): ")
Vault[int(Coordinates[0])-1][int(Coordinates[1])-1]="X"
print(f"{Vault[0]}\n{Vault[1]}\n{Vault[2]}")