# 6) შექმენით ინტეჯერების ლისტი, და ორი ცვლადი positive, negative. გამოიტანეთ სიაში არსებული დადებითი რიცხცების ჯამი, უარყოფითები რიცხვების რაოდენობა და დაპრინტე "zero" რამდენჯერაც შეგხვდება 0

# 6) შექმენით ინტეჯერების ლისტი, და ორი ცვლადი positive, negative. გამოიტანეთ სიაში არსებული დადებითი რიცხცების ჯამი, უარყოფითები რიცხვების რაოდენობა და დაპრინტე "zero" რამდენჯერაც შეგხვდება 0

numbers = [1, 0, 5, -6, 7, 3, -12, 7, -3, -1, 0, 5, 0]

positive = 0
negative = 0

for i in numbers:
    if i > 0:
        positive += i
    elif i < 0:
        negative += 1
    else:
        print("zero")

print(f"Positive Sum = {positive}")
print(f"Negative sum = {negative}")