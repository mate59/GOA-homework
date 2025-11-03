# 1) შემოაყვანიეთ მომხმარებელს რაღაცა სიტყვა:
# -> შეამოწმეთ არის თუ არა 'a' ან 'A' ამ სიტყვაში/ტექსტში
# -> შეამოწმეთ თუ "არ" არის სიტყვა 'car' ამ სიტყვაში/ტექსტში


inputt = input("enter something: ")

if "a" in inputt or "A" in inputt:
    print("არის ან a ან A")

else:
    ("არ არის")


inppuutt = input("enter something")

if "car" not in inputt:
    print("car არ არის")

else:
    print("car არის")


# 2) მომხმარებელს შემოატანინეთ ტექსტი.
# -> დაუარეთ ამ ტექტის ასოებს for ლუპით
# -> თუ ასო არის 'a' ან 'A' დასკიპეთ, სხვა შემთხვევაში დაპრინტეთ ასო


text = input("enter text: ")

for text in text:
    if text == 'a' or text == 'A':
        continue
    print(text)







