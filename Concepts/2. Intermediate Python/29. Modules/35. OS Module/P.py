# Clear the Clutter

import os
files=os.listdir("ProjectFolder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"ProjectFolder/{file}",f"ProjectFolder/{i}.png")
        i+=1