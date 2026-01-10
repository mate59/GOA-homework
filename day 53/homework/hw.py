# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

words = ["keyboard" , "Mouse" , "goga" , "BMW"]

newlist = []

for i in words:
    if i.islower() and i[0] == "g":
        newlist.append("Goga")
    elif i.isupper() or i[0] == "N":
        newlist.append("Nika")
    else:
        newlist.append("ლიდერი")

print(newlist)



























