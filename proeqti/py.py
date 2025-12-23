words = ["qwe" , "rty" , "uiOP" , "asDF"]

new_list = [1, 2, 3, 4, 5]

for i in words:
    if words.index(i) % 2 == 1 and i[-2:] == i[-2:].upper():
        new_list.insert(0, i)

print(new_list)





