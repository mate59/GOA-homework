# #კომენტარის სახით ახსენი თუ რომელი ოპერატორები ვისწავლეთ და რა დანიშნულება აქვთ მათ

# # #მინიჭების ოპერატორი - ვადარებთ რიცხვებს და ვანიჭებთ true და false-ს
print(10>5)#true
print(10<5)#false
print(14==15)#false

# # #მომხმარებელს შემოაყვანინეთ ორი რიცხვი,შეადარეთ თუ პირველი რიცხვი მეტია მეორეზე,ასევე შეადარე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე,და ასევე შეადარე თუ პირველი რიცხვი უდრის მეორე რიცხვს
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print(num1>num2)
print(num1<num2)
print(num1=num2)

# #მომხმარებელს შემოატანინეთ 5 სტრინგ ტიპის მნიშვნელობა,შენი დავალებაა მოახდინო მათი კონკატინაცია
word1 = (input("enter your name: "))
word2 = (input("enter your surname: "))
word3 = (input("enter the country where your from: " ))
word4 = (input("enter your height: "))
word5 = (input("enter your weight: "))

# print(word1 + word2 + word3 + word4 + word5)

#მომხმარებელს შემოატანინე 4 რიცხვი,შენი დავალებაა გაიგო ამ რიცხვების საშუალო არითმეტიკული
math1 = int(input("enter first number: "))
math2 = int(input("enter second number: "))
math3 = int(input("enter third number: "))
math4 = int(input("enter fourth number: "))

print((math1 + math2 + math3 +math4) / 4)

# # #შექმენი 4 ცვლადი,ამ ცვლადებშ შეინახე 4 განსხვავებული მონაცემთა ტიპის ელემენტები და დაპრინტე მათ ტიპი

name = "mate"
surname = "arabuli"
num1 = 13
num2 = 1.75


print(type(name))
print(type(surname))
print(type(num1))
print(type(num2))

# #შექმენი 2 ცვლადი,შეინახე ორივე ცვლადში სტრინგ ტიპის მნიშვნელობები დაშეადარე ისინი არიან თუ არა ერთნაირები
str1 = "homework"
str2 = "homework"

print(str1 == str2)

str3 = "homework"
str4 = "classwork"

print(str3 == str4)

# #შექმენი 4 ცვლადი,სადაც გექნება მოთავსებული რიცხვები ოღონდ სტრინგის სახით მაგ: "40",გადაიყვანე ეს სტრინგი რიცხვები ინტეჯერში(გამოიყენე შესაბამისი ფუნქცია) და გაიგე ამ ოთხი რიცხვის ჯამი
num1 = int("10")
num2 = int("25")
num3 = int("49")
num4 = int("124")

print(num1 + num2 + num3 + num4)

# #შექმენი 3 ცვლადი,ამ ცვლადებში შეინახეთ ინტეჯერ ტიპის მონაცემები,შენი დავალებაა ეს რიცხვები გაასტრინგო(გამოიყენე შესაბამისი ფუნქცია) და გამოიტანო ეს რიცხვები ერთ წინადადებაში. მაგ:304050
num5 = str(20)
num6 = str(40)
num7 = str(10)

print(num5 + num6 + num7)

