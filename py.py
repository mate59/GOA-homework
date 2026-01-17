# num = ["gela", "Keyboard", "mouse", "Mate", "Nika"]

# num1 = []

# i = 0

# while i < len(num):
#     if num[i] == num[i].capitalize() and i % 2 == 0:
#         num1.append(num[i])
#     i += 1

# print(num1)


# 1) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, ანუ წერია lowercase-ში, ამ სიტყვის ყველა ასო გახადეთ დიდი.
# თუ სიტყვა შეიცავს თუნდაც ერთ uppercase ასოს, ეს სიტყვა ამოშალეთ სიიდან. ბოლოს დაპრინტეთ მიღებული სია. (არ შექმნათ ახალი სია, იმუშავეთ პირველ სიტყვების სიაში) გამოიყენეთ while ციკლი.


num = ["gela", "Keyboard", "mouse", "Mate", "Nika"]

i = 0

while i < len(num):
    if num[i] == num[i].lower():
        num[i] = num[i].upper()
        i += 1
    else:
        num.remove(num[i])
    

print(num)







