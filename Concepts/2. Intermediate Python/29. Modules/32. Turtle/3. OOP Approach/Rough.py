import colorgram
colors=colorgram.extract("Ada.jpg",10)
colors_list=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    colors_list.append(new_color)
print(colors_list)

"""
O/p: [(16, 22, 47), (124, 92, 60), (47, 13, 34), (205, 149, 95), (181, 11, 56), (52, 40, 29), (241, 50, 89), (170, 45, 79), (175, 127, 70), (245, 224, 191)]
"""