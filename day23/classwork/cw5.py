# 5)მომხმარებელს შემოატანინე მისი გვარი, შემდეგ შეეიკითხე რომელ case-ში უნდა რომ მისი გვარი დაიწეროს (თუ შემოიტანა upper, დაუბეჭდეთ მისი გვარი გადიდებულად / თუ შემოიტანა lower, დაუბეჭდეთ მისი გვარი დაპატარავებული ასოებით / თუ შემოიტანა capitalize, პირველი ასო გაადიდეთ დანარჩენი დააპატარავეთ, თუ შემოიტანა none მაშინ არ შეცვალოთ და სხვა შემთხვევაში დაუბეჭდეთ incorrect input

surname = input("enter your surname: ")
case = input("In which case would you like us to write your name? ")

if case == 'upper':
    print(surname.upper())
elif case == 'lower':
    print(surname.lower())
elif case == 'capitalize':
    print(surname.capitalize())
elif case == 'none':
    print(surname)
else:
    print('incorrect input')