#1) შემოატანინეთ მომხმარებელს 3 რიცხვი, შეამოწმეთ:
# თუ 1 და 2 რიცხვი ტოლია -> დაწერეთ 1 და 2 ტოლია
# თუ 1 და 3 რიცხვი ტოლია -> დაწერეთ 1 და 3 ტოლია
# თუ 2 და 3 რიცხვი ტოლია -> დაწერეთ 2 და 3 ტოლია
# თუ სამივე ტოლია -> დაწერეთ სამივე ტოლია
# თუ არცერთი არ არის ტოლი -> დაწერეთ არცერთი არ არის ტოლი

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 == num2 == num3:
        print("სამივე ტოლია")
elif num1 == num2:
        print("1 და 2 ტოლია")
elif num1 == num3:
        print("1 და 3 ტოლია")
elif num2 == num3:
        print("2 და 3 ტოლია")
else:
        print("არცერთი არ არის ტოლი")

#2) შემოატანინეთ მომხმარებელს რიცხვი 1-დან 12ჩათვლით:
# თუ ეს რიცხვი არის 12, 1, 2 -> დაპრინტეთ ზამთარი
# თუ ეს რიცხვი არის 3, 4, 5 -> დაპრინტეთ გაზაფხული
# თუ ეს რიცხვი არის 6, 7, 8 -> დაპრინტეთ ზაფხული
# თუ ეს რიცხვი არის 9, 10, 11 -> დაპრინტეთ შემოდგომა

num = int(input("Enter a number between 1 and 12: "))

if num == 12 or num == 1 or num == 2:  
    print("ზამთარი")
elif num == 3 or num == 4 or num == 5:
    print("გაზაფხული")
elif num == 6 or num == 7 or num == 8:
    print("ზაფხული")
elif num == 9 or num == 10 or num == 11:
    print("შემოდგომა")

#3) შემოატანინეთ მომხმარებელს თავისი სახელი:
# თუ სახელი უდრის admin:
#    მოთხოვეთ შემოიყვანოს ადმინის პაროლი:
#       თუ პაროლი უდრის adminpassword123:
#         დაპრინტეთ სალამი ადმინ
#       სხვა შემთხვევაში:
#         დაპრინტეთ წვდომა არ გაქვს
# სხვა შემთხვევაში:
#   დაპრინტეთ სალამი მომხმარებელო

if input("Enter your name: ") == "admin":
    if input("Enter admin password: ") == "adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")








    #aniwebs upiratesobas trues da andi false
    