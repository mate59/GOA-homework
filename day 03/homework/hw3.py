num1 = 120
num2 = 80

sum_of_numbers = num1 + num2
sum_of_numbers = num1 - num2
sum_of_numbers = num1 * num2
sum_of_numbers = num1 / num2

name = "Mate"
name = "saba"
name = "nikolozi"
name = "sandro"
name = "pavle"

print(name)

name = "pirveli cvladi"
Name = "meore cvladi"
NAME = "mesame cvladi"
nAme = "meotxe cvladi"
naMe = "mexute cvladi"

print(name)
print(Name)
print(NAME)
print(nAme)
print(naMe)

name = "giorgi"   #რიცხვით დაწყება გამოსახავს ერორს
user_name = "bubunauri"   #გამოტოვების (ან }) ნაცვლად იწერება ქვედა ხაზი
user_name = "goga"   #ბოლოს გამოსახულ სტრინგს ყოველთვის სჭირდება ბრჭყალები
user_surname = "axalaia"   #აქ შესაცვლელი იყო ქვედა ხაზი და ბრჭყალები

first_name = "mate"
last_name = "arabuli"
age = "13"
city = "tbililsi"
hobby = "biker"

full_sentence = first_name +  " " + last_name + " " + age + " " + city + " " + hobby

print(full_sentence)

name = "mate"
times = 13

result = name * times

print (result)

name = "mate"  # სტრინგი
number = 45    # ინტეჯერი

# 1. სტრინგი + ინტეჯერი - დაგვიბრუნებს შეცდომას, რადგან არ შეგვიძლია მათ გამატება პირდაპირ
# print(name + number)  # TypeError: can only concatenate str (not "int") to str

# 2. სტრინგი - ინტეჯერი - ასევე არ შეგვიძლია, რადგან სტრინგზე რიცხვების გამოკლება შეუძლებელია
# print(name - number)  # TypeError: unsupported operand type(s) for -: 'str' and 'int'

# 3. სტრინგი / ინტეჯერი - არ შეგვიძლია, რადგან არ არის შესაძლებელი სტრინგის გრძივობა და რიცხვის გამყოფი
# print(name / number)  # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# 4. სტრინგი * სტრინგი - არ შეგვიძლია, რადგან სტრინგების გამრავლება მხოლოდ რიცხვთან შეიძლება
# print(name * name)  # TypeError: can't multiply sequence by non-int of type 'str'