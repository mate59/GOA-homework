# 1) მომხმარებელს შემოატანინეთ სიტყვა.  
# -> იტერაციით გაიარეთ თითო ასო  
# -> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)  
# -> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო  


inputt = input("enter a word: ")

for i in inputt:
    if i == "e" or i == "E":
        break
    else:
        print(i)



# 2) მომხმარებელს შემოატანინეთ წინადადება.  
# -> შეამოწმეთ არის თუ არა ტექსტში სიტყვა 'bad'  
# -> თუ არის, დაპრინტეთ "აკრძალული სიტყვა!"  
# -> თუ არაა, დაპრინტეთ "ყველაფერი რიგზეა"  


zxcv = input("enter a sentence: ")

if "bad" in zxcv:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")



# 3) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ ტექსტს for ციკლით  
# -> გამოტოვეთ ყველა space => ' '
# -> დაბეჭდეთ ყველა დანარჩენი სიმბოლო  


zxcvb = input("enter a word: ")

for i in zxcvb:
    if i == " ":
        continue
    print(i)



# 4) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ მას for ლუპით  
# -> გამოტოვეთ ხმოვნები (a, e, i, o, u)  
# -> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო 


zxcvbnm = input("enter a word: ")

for i in zxcvbnm:
    if i in "aeiou":
        continue
    print(i)



# 5) მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)


num1 = int(input("enter first number: "))

num2 = int(input("enter second number: "))


for i in range(num1, num2):
    if i % 15 == 0:
        print(i)
        break



# 6) შექმენით უსასრულო while loop:
# --> სანამ მომხმარებელი არ შემოიყვანს 'python is best', მანამდე დაპრინტეთ 'you should learn python'


while True:
    user_input = input("enter a phrase: ")
    if user_input == "python is best":
        break
    print("you should learn python")



# 7) \<.BOSS.>/ 
# მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)


num2 = int(input("enter first number: "))

num3 = int(input("enter second number: "))

count = 0

for i in range(num2, num3):
    if i % 3 == 0:
        count += 1
        if count == 3:
            print(i)
            break
