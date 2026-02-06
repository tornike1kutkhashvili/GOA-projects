# 7)შექმენით სახელების სია შემდეგ გადაუარეთ და შეამოწმეთ რომელი სახელიც იწყება "g" ასოთი დაბეჭდეთ ეს სახელი და გვერდით მიუწერეთ True

names = ["gio", "nika", "goga", "ana", "giorgi", "luka"]

for name in names:
    if name.startswith("g"):
        print(name, True)