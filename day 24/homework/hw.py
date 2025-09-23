# 1)შექმენი სია 7 რიცხვით.

# დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.

# დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).


# numbers = [2, 4, 6, 8, 10, 12, 14]


# print(numbers[-1])
# print(numbers[-7])



# # # #2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".

# # # # დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.


# fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]

# print(fruits[2])
# print(fruits[3])

# print(fruits[-3])
# print(fruits[-4])


# # 3)
# # შექმენი [3,4,5,6,7,1,2,9,8,11]

# # მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.

# # თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი

# # თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "


# numbers = [3,4,5,6,7,1,2,9,8,11]

# index = int(input("Enter an index (0-9): "))

# if 0 < index < 10:
#     print(numbers[index])
# else:
#     print("you entered negative or more than 10  number ")


# # #4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]


# # # --- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in the forest very fast"

# # # --- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით

# # # --- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "the cat is very angry"


# list = ["dog" ," most" ,"is" ,"angry" ,"running", "the" , "forest", "fast", "in" , "cat" ,"human", "very"]


# print(list[-12])
# print(list[-10])
# print(list[-8])
# print(list[-4])
# print(list[-7])
# print(list[-6])
# print(list[-1])
# print(list[-5])

# print(list[5])
# print(list[9])
# print(list[2])
# print(list[11])
# print(list[3])


# # # 5)
# # # 5)
# # # შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
# # # მომხმარებელს შემოიტანინე ინდექსი(რიცხვი)

# # # თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე "შენ აირჩიე კატა".

# # # თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".

# # # სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".

# animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]

# index = int(input("Enter an index (0-5): "))

# if animals[index] == "cat":
#     print("შენ აირჩიე კატა.")
# elif animals[index] == "goat":
#     print("შენ აირჩიე თხა.")
# else:
#     print("სხვა ცხოველი აირჩიე.")


# # # 6)
# # # შექმენი სია 6 ქალაქით.
# # # მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).

# # # თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.

# # # თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.

# # # თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი ვთქვათ თუ შემოიყვანა მომხმარებელმა 5 და 5 დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.

# cities = ["Tbilisi", "Batumi", "Zugdidi", "Kutaisi", "Rustavi", "Zestafoni"]

# index1 = int(input("Enter the first index (0-5): "))
# index2 = int(input("Enter the second index (0-5): "))

# if index1 < index2:
#     print(cities[index1])
#     print(cities[index2])
# elif index1 > index2:
#     print("შეცვალე ინდექსები ადგილებით")
#     print(cities[index2])
#     print(cities[index1])
# else:
#     print("ორივე ერთია")
#     print(cities[index1])


# # #7)მომხმარებელი შემოიტანს სიტყვას.

# # # თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".

# # # თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".

# # # სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".


# index = int(input("enter a symbol: "))

# word = ("a")

# word2 = ("z")


# if index == word:
#     print("სიტყვა იწყება a-თი")

# elif index == word2:
#     print("სიტყვა მთავრდება z-თი ")

# else:
#     print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")



# #8)დავალება 4

# # მომხმარებელი შემოიტანს სიტყვას.

# # თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".

# # თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".



# sityva = input("enter a word: ")

# sityva2 = input("enter a second word: ")

# if sityva == sityva2:
#     print("პირველი და ბოლო ერთნაირია")
# else:
#     print("პირველი და ბოლო განსხვავებულია")


# #9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
 

# # ----ამ სიიდან შეადგინე სიტყვა "goga, 

# # ----ამ სიტყვიდან შეადგინე სიტყვა "saba"

# # ----ამ სიტყვიდან შეადგინე სიტყვა "bativar"


# cvladi = "agivorsbgitr"

# print(cvladi[1])
# print(cvladi[4])
# print(cvladi[1])
# print(cvladi[0])


# print(cvladi[6])
# print(cvladi[0])
# print(cvladi[7])
# print(cvladi[0])


# print(cvladi[7])
# print(cvladi[0])
# print(cvladi[10])
# print(cvladi[2])
# print(cvladi[3])
# print(cvladi[0])
# print(cvladi[5])


#10)შექმენი შემდეგი სტრინგი --> 'giorgi'

# შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე



string = 'giorgi'


for i in string:
    print(i)


#??????










