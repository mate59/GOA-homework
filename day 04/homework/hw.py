#input - შეაქვს ინფორმაცია საიტში
#output - გამოაქვს ინფორმაცია საიტიდან

value = input("2011")

print("Mate", value)
print("birthday", type(value))

name = "Mate"          
city = "Tbilisi"        
language = "Python"     
email = "matearabuli8@gmail.com"  
country = "Georgia"     

age = 13                
year = 2011             
students = 28           
height_cm = 178        
books = 0             

price = 19.99           
weight = 62.4           
temperature = 35.6      
height_m = 1.78        
π = 3.1415             

name = "Mate"    
age = 13           
height = 1.78
print("name", type(name))     # class 'str'
print("age", type(age))       # class 'int'
print("height", type(height)) # class 'flo'

word1 = input("Volkswagen")
word2 = input("Skoda")

result = word1 + word2

print(result)

num1 = float(input("2.6"))
num2 = float(input("1.78"))
num3 = float(input("3.1415"))
num4 = float(input("7.45"))
num5 = float(input("15.24"))

average = (num1 + num2 + num3 + num4 + num5)

print(average)


first_name = input("mate")
last_name = input("arabuli")
age = int(input("13"))
height = float(input("1.78"))
weight = float(input("62.4"))

print("გამარჯობა, მე ვარ {first_name} {last_name}, {age} წლის, სიმაღლე მაქვს {height} მეტრი და ვიწონი {weight} კილოგრამი.")