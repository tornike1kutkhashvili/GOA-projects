# 5)შექმენით ცვლადი სადაც შეინახავთ ორიგინალ აქაუნთის პაროლს, და while ციკლის მეშვეობით მომხმარებელს შეეკითხეთ აქაუნთის პაროლი იქამდე სანამ სწორედ არ გამოიცნობს.

password = 12345678
user = int(input("enter your password: "))
while password != user:
    user = int(input("enter your password: "))

print('correct')