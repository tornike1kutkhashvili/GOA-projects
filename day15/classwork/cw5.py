# 5)მომხმარებელს შემოატანინე მისი საყვარელი ფილმი და სახელი, თუ მისი სახელი ავთოა მაშინ დაპრინტე "you are avto" , თუ ლევანი ქვია და მისი საყვარელი ფილმია ტიტანიკი, დაპრინტე "Levani loves titanic" ყველა სხვა შემთხვევაში დაპრინტე "someone likes other film" 

name = input("შეიყვანე შენი სახელი: ")
movie = input("შეიყვანე შენი საყვარელი ფილმი: ")

if name == "ავთო":
    print("you are avto")
elif name == "ლევანი":
    if movie == "ტიტანიკი":
        print("Levani loves titanic")
    else:
        print("someone likes other film")
else:
    print("someone likes other film")