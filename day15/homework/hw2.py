# 2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

age = 4
age1 = int(input("enter yout favourite number: "))
if age == age1:
    print("perfect")
elif age1 >  age:
    print("more")
else:
    print("less")