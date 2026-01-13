# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

words = ["keyboard" , "Mouse" , "goga" , "BMW"]

newlist = []

for i in words:
    if i.lower() and i[0] == "g":
        newlist.append("Goga")
    elif i.upper() or i[0] == "N":
        newlist.append("Nika")
    else:
        newlist.append("ლიდერი")

print(newlist)


# 3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

newlist = []

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0 or i % 2 == 0:
        newlist.append(numbers[i] ** 2)
    else:
        newlist.append(numbers[i] * 2)
    i += 1

print(newlist)


# 4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words = ["keyboard", "Mouse", "goga", "BMW", "Nika"]

newlist = []

i = 0

while i < len(words):
    if len(words[i]) > 6 or words[i].isupper():
        newlist.append(words[i].lower())
    else:
        newlist.append(words[i] + words[i])
    i += 1

print(newlist)


# 5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.


numbers = "0123456789"
newlist = []

for i in range(len(numbers)):
    if i % 2 == 0 or int(numbers[i]) > 7:
        newlist.append(int(numbers[i]))

print(newlist)























