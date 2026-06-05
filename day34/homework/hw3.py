names = {"Giorgi", "Nika", "Luka"}

user_name = input("შეიყვანე სახელი შენი და არა სხვისი ტყუილების გარეშე:  ")

if user_name in names:
    print("ეს სახელი არის სეტში და აღარ დაემატება(ბანძი სახელია და მაგიტო)")
else:
    names.add(user_name)
    print("სახელი დაემატა")
    print(names)