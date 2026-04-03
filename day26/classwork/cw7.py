# 7)შექმენით sum ფუნქციის იდენტური ვარიანტი (sum ფუნქციას გადაეცემა ინტეჯერების სია და გამოაქ ამ ინტეჯერების ჯამი)

def sum(list):
    sul = 0
    for num in list:
        sul += num
    print(sul)