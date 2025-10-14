# 1)შექმენით სია -->  ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"] , თქვენი დავალებაა რომ პირველი 2 ელემენტი ჩაანაცვლოთ შემდეგი სიით --> ["irina" , "milana" , "kira", "mate"] //////////////// და ასევე სიის ბოლო ორი ელემენტი შეანაცვლე შემდეგი სიით --> ["gia" , "emzari" , "xvicha"] ამის შემდეგ დაპრინტეთ საბოლოო სია


list1 = ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"]

list1[:2] = ["irina" , "milana" , "kira", "mate"]

list1[4:] = ["gia" , "emzari" , "xvicha"]

print(list1)

#2)შექმენით ცვლადი და მომხმარებელს შემოატანინეთ რიცხვი,თუ რიცხვი ლუწია დაუპრინტეთ "EVEN" შემდეგ შეამოწმეთ თუ რიცხცვი არის კენტი დაუპრინტეთ "Odd"

input = int(input("ener a number: "))

if input % 2 == 0:
    print("ეს რიცხვი არის even")
elif input % 2 == 1:
    print("ეს რიცხვი არის odd")
else:
    print("შემოიტანე რიცხვი!!!")

