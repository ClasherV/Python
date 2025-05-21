import os
files=os.listdir("Beloved Ada")
i=1
for file in files:
    if file.endswith(".png"):
        if file.endswith("7.png"):
            continue
        else:
            print(file)
            os.rename(f"Beloved Ada/{file}",f"Beloved Ada/{i}.jpg")
            i+=1