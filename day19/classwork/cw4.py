# 4)შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს თავის გვარს, თუ პირველი 5 ასო შენი გვარის პირველი 5 ასოს მსგავსია, დაპრინტე 'almost same' სხვა შემთხვევაში დაპრინტე 'bye'

my_name = 'kutkhashvili'
surname = input("enter your surname: ")

if surname[:5] == my_name[:5]:
    print('almost same')
else:
    print('bay')