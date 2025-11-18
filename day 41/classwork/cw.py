# 1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

listi = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

listi.append("ianvari")

print(listi)


# 2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

lissti = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

lissti.insert( 1 , "bati" )

print(lissti)


# 3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა

llisti = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

llisti.pop(4)

print(llisti)


# 4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა

llistii = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

llistii.pop(5)

llistii.pop(3)

print(llistii)
