# 4)დაწერე ფუნქცია, რომელიც დააბრუნებს მხოლოდ ლუწ რიცხვებს ახალი list-ის სახით

def even_numbers(numbers):                           
    list = []
    if numbers % 2 == 0:
        list.append(numbers)   
    else:
        print('inccorect')
    print(list)

even_numbers(4)
