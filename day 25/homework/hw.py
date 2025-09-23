# 1)შექმენი სია 7 რიცხვით.

# დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.

# დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).


numbers = [2, 4, 6, 8, 10, 12, 14]


print(numbers[-1])
print(numbers[-7])



#2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".

# დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.


fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]

print(fruits[2])
print(fruits[3])

print(fruits[-3])
print(fruits[-4])


#3)
# შექმენი [3,4,5,6,7,1,2,9,8,11]

# მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.

# თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი

# თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "


numbers1 = [1,2,3,4,5,6,7,8,9,10]


idk = int(input("enter a number between 0 and 10"))


if idk == numbers1:
    print("თქვენი ინდექსი დადებითია")          #??????

else:
    print("თქვენ რიცხვი უარყოფითია ან მეტი 10-ზე")



#4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]


# --- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in the forest (very) fast"

# --- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით

# --- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "the cat is very angry"


list = ["dog" ," most" ,"is" ,"angry" ,"running", "the" , "forest", "fast", "in" , "cat" ,"human", "very"]


print(list[-11])
print(list[-9])
print(list[-7])
print(list[-4])
print(list[-7])
print(list[-6])












