# 4)დაწერე პროგრამა, რომელიც ამოწმებს რიცხვი არის თუ არა ის ერთდროულად 3-ისა და 5-ის ჯერადი.

favourite_number = int(input("enter your favourite number:"))
if favourite_number % 3 == 0:
    if favourite_number % 5 == 0:
        print("best number")
else:
    print('bad number5')