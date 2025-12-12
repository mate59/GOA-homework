# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

names = ["Mate" , "nika" , "Saba" , "goga" , "Nino"]

Upper_name = []

for name in names:
    if name[0] == name[0].upper():
        Upper_name.append(name)

print(Upper_name)


# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული შედეგი.

names = ["Mate", "Nika", "Saba"]

surnames = ["arabuli" , "geladze" , "jorashvili"]

for i in names:
    names = [name.upper() for name in names]
    surnames = [surname.lower() for surname in surnames]

print(surnames)


# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება დიდი ასოთი.

words = ["qwer" , "tyuioop" , "Asdfg" , "Hjklk"]

for i in words:
    if len(i) < 6 or i[-1] == i[-1].upper():
        words.remove(i)

print(words)


# 4) შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.

ricxvebi = [12.5, 7.8, 45.3, 102.4, 88.9, 9.1, 67.2, 150.6, 23.4, 55.5]

new_list = []

for i in ricxvebi:
    if 10 < i < 100:
        new_list.append(i)

print(new_list)


# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Zugdidi"]

countries = ["Georgia", "Armenia", "Azerbaijan", "Turkey", "Russia", "Ukraine", "Belarus", "Poland", "Germany", "France"]


for i in range(len(countries)):
    countries[i] = countries[i] + cities[i][1:5]

print(countries)






