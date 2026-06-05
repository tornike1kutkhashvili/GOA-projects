# 2)გვაქვს tuple-ში შემდეგი ელემენტები banana,cucumber,tomato,apple და სამი ცვლადი green red და yellow
# დაალეგე ეს ელემენტები tuple ში ისე რომ unpacking-ის შემდეგ ყველა ცვლადში შესაბამისი ფერის მქონე იყოს
# (ცვლადების მიმდევრობა არ უნდა შეცვალო, უნდა იყოს green, red და yellow)

fruits = ("banana", "cucumber", "tomato", "apple")

fruits_list = list(fruits)

fruits_list = ["cucumber", "apple", "tomato", "banana"]

fruits = tuple(fruits_list)

*green, red, yellow = fruits

print(green)
print(red)
print(yellow)
