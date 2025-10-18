# for ლუპით დაუარეთ რიცხვებს 0 დან 100 ჩათვლით, თუ რიცხვი(i) კენტია დაბეჭდეთ 'კენტია' თუ რიცხვი(i)ლუწია დაბეჭდეთ 'ლუწია'. თუ რიცხვი(i) ნულია დაბეჭდეთ 'ნული'
# for i in range(0, 101)

for i in range(101):
    if i == 0:
        print(i, "the number is 0")
    elif i % 2 == 0:
        print(i, "the number is odd")
    else:
        print(i, "the number is even")



