# 3)დაწერე ფუნქცია, ფუნქცია ამოწმებს, არის თუ არა სიტყვა პალინდრომი (მაგ: "level"). (პალინდრომი არის სიტყვა რომელიც წაღმაც და უკუღმაც იგივე გამოდის)

def palindrom(str):
    if str == str[::-1]:
        print('palindrom')
    else:
        print('inccorect')


palindrom('goa')