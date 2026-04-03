# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი და ინტეჯერი, ასევე ფუნქციას ქონდეს სია რომელშიც ჩაამატებ მომხმარებლის შემოტანილ სტრინგს იმ ინდექსზე რომელიც მან შემოიტანა

user = input("შეიყვანე სტრინგი: ")
index = int(input("შეიყვანე ინდექსი: "))

def insert_string(user_string, index):
    list = []

    if index > len(list):
        list.append(user_string)
    else:
        list.insert(index, user_string)

print(list)

print(insert_string(user, index))