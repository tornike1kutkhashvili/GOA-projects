# 3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ
# თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height: "))

if age > 18 and name == "tornike" and height > 1.80:
    print("right")
else:
    print("inccorect")