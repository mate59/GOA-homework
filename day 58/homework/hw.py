# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

words = ["GELA" , "mausi" , "VAJA" , "vigac"]

words1 = []

for i in words:
    if i.isupper():
        words1.append(i)

print(words1)


# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.

inputi = input("enter a sentence: ")

words = inputi.split()
i = 0
count = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print(count)






















































