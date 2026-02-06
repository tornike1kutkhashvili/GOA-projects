# 5)შექმენით სახელების სია და მომხმარებლებს შემოატანინეთ მისი სახელი ასევე count ცვლადი, გადაუარეთ ამ სიას და რამდენჯერაც 
# მომხმარებლის სახელი შეგხვდებათ დაპრინტე "user name" და count მოუმატე ერთი საბოლოოდ  დაპრინტე count ცვლადი

names = ["gio", "nika", "ana", "gio", "luka", "gio"]

user_name = input("შეიყვანე შენი სახელი: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print("count =", count)