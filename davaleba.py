def filter_list(l):
    integer = []
    for i in l:
        if type(i) == int:     
            integer.append(i)
    return integer


print(filter_list([1 , 12,'goa']))