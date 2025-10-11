# 1)მოცემულია სტრინგი "PythonProgramming".
# ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing

word = "PythonProgramming"

print(word[:6])


#2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
# ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)

list = [10, 20, 30, 40, 50, 60, 70]

print(list[-5:-2])


# 3)მოცემულია სტრინგი "HelloWorld".
# დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)

word1 = "HelloWorld"

print(word1[:5])
print(word1[:-5])


# 3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
# დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[0:1])
print(letters[-7:-6])

print(letters[2:3])
print(letters[-5:-4])

print(letters[4:5])
print(letters[-3:-2])


# 4)მოცემულია სტრინგი "Information".
# ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)

word2 = "Information"

print(word2[2:7])
print(word2[-9:-4])


# 5)მოცემულია სტრინგი "abcdefghijklmno".
# შექმენი სამი სხვადასხვა სლაისი:

# პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს

# მეორე – შეიცავდეს j დან o მდე ასოებს

# მესამე – შეიცავდეს f დან j მდე ასოებს

word3 = "abcdefghijklmno"

print(word3[0:1])
print(word3[-2:-1])
print(word3[3:4])


























