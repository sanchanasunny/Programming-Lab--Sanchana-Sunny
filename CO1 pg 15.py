#Print out all colors from color-list1 not contained in color-list2. 

color_list_1 = set(["White", "Black", "Red","Blue"])
color_list_2 = set(["Red", "Green","pink"])

print(color_list_1.difference(color_list_2))