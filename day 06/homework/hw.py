num1 = (int(input("enter first number: ")))
num2 = (int(input("enter second number: ")))

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)


num3 = "90"
num4 = "40"
num5 = "25"
num6 = 55
num7 = 30

print((int(num3) * int(num4) * int(num5) * num6 * num7) / 5)
print(type("10" * 5))

word1 = input("enter first word: ")
word2 = input("enter second number: ")
word3 = input("enter third number: ")
int1 = int(input("enter your number: "))
word_sum = word1 + word2 +word3
print(word_sum * int1)

#and - ერთი პირობა თუ იქნება false, პასუხიც იქნება false
#or - ერთი პირობა თუ იქნება true, პასუხიც იქნება true

# True and True -- true იმიტომ რომ ორივე არის true       |   True or True -- true იმიტომ რომ ორივე არის true          
# True and False -- false იმიტომ რომ ერთი არის false     |   True or False -- false იმიტომ რომ ერთი არის false
# False and True -- false იმიტომ რომ ერთი არის false     |   False or True -- false იმიტომ რომ ერთი არის false
# False and False -- false იმიტომ რომ ორივე არის false    |   False or False -- false იმიტომ რომ ორივე არის false

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

word1 = "GOA"
num1 = 32
num2 = 50.99
bool = True
print(type(word1))
print(type(num1))
print(type(num2))
print(type(bool))

flo1 = float(input("enter your number: "))
int1 = int(input("enter your number: "))
str1 = input("enter your name: ")

print(flo1)
print(int1)
print(str1)
