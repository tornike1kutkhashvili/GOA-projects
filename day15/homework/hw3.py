# 3)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს ასაკს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".

age = int(input("enter your age: "))
name = input("enter your name: ")
if name == 'tornike':
    if age == 15:
        print("twins")
else:
    print("not twins")