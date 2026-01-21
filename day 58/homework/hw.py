# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

words = ["GELA" , "mausi" , "VAJA" , "vigac"]

words1 = []

for i in words:
    if i.isupper():
        words1.append(i)

print(words1)


# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.

inputi = input("enter a sentence: ")

i = 0

count = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print(count)


# 3) მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ ზუსტად იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True, თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].

word = input("enter a word: ")

for i in word:
    if word[i] == word[i].reverse():
        print("true")

    if word[i] != word[i].reverse():
        print("false")


# 4) შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.

scr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

scr1 = []

scr2 = []

for i in scr:
    if i % 2 == 0 and i % 2 == 1:
        scr1.append(i)

    if i % 2 == 1 and i % 2 == 1:
        scr2.append(i)

print(scr1)
print(scr2)


# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.

mon = ["mate" , 0 , 4 , 3, 2 , True, False]

i = 0

while i < len(mon):
    if mon.count(mon[i]) > 1:
        mon.remove(mon[i])
    else:
        i += 1

print(mon)


# 6) მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

win = input("enter a sentence: ")

words = win.split()

i = 0

longest = ""

while i < len(words):
    if len(words[i]) > len(longest):
        longest = words[i]
    i += 1

print(longest)




