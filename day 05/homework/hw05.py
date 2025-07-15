# #კომენტარის სახით ახსენი თუ რომელი ოპერატორები ვისწავლეთ და რა დანიშნულება აქვთ მათ

# #მინიჭების ოპერატორი - ვადარებთ რიცხვებს და ვანიჭებთ true და false-ს
print(10>5)#true
print(10<5)#false
print(14==15)#false

# #მომხმარებელს შემოაყვანინეთ ორი რიცხვი,შეადარეთ თუ პირველი რიცხვი მეტია მეორეზე,ასევე შეადარე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე,და ასევე შეადარე თუ პირველი რიცხვი უდრის მეორე რიცხვს
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

print(num1>num2)
print(num1<num2)
print(num1=num2)

# #მომხმარებელს შემოატანინეთ 5 სტრინგ ტიპის მნიშვნელობა,შენი დავალებაა მოახდინო მათი კონკატინაცია
str(input("enter your name: "))
str(input("enter your surname: "))
str(input("enter the country where your from: " ))
str(input("enter your height: "))
str(input("enter your weight: "))

# #მომხმარებელს შემოატანინე 4 რიცხვი,შენი დავალებაა გაიგო ამ რიცხვების საშუალო არითმეტიკული
input("enter first number: ")
input("enter second number: ")
input("enter third number: ")
input("enter fourth number: ")

#??? ვერ გავიგე, როგორ უნდა გავყო?

# #შექმენი 4 ცვლადი,ამ ცვლადებშ შეინახე 4 განსხვავებული მონაცემთა ტიპის ელემენტები და დაპრინტე მათ ტიპი
print(type("mate"))
print(type("arabuli"))
print(type(13))
print(type(1.75))

#შექმენი 2 ცვლადი,შეინახე ორივე ცვლადში სტრინგ ტიპის მნიშვნელობები დაშეადარე ისინი არიან თუ არა ერთნაირები
str1 = "homework"
str2 = "homework"

print(str1 == str2)

str3 = "homework"
str4 = "classwork"

print(str3 == str4)

#შექმენი 4 ცვლადი,სადაც გექნება მოთავსებული რიცხვები ოღონდ სტრინგის სახით მაგ: "40",გადაიყვანე ეს სტრინგი რიცხვები ინტეჯერში(გამოიყენე შესაბამისი ფუნქცია) და გაიგე ამ ოთხი რიცხვის ჯამი
num1 = int("10")
num2 = int("25")
num3 = int("49")
num4 = int("124")

print(num1 + num2 + num3 + num4)

#შექმენი 3 ცვლადი,ამ ცვლადებში შეინახეთ ინტეჯერ ტიპის მონაცემები,შენი დავალებაა ეს რიცხვები გაასტრინგო(გამოიყენე შესაბამისი ფუნქცია) და გამოიტანო ეს რიცხვები ერთ წინადადებაში. მაგ:304050
num5 = str(20)
num6 = str(40)
num7 = str(10)

print(num5 + num6 + num7)

