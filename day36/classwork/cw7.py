# 6) შექმენი ორი სეტი და გამოიტანე ელემენტები რომელიც ერთ სეტში არის და მეორეში არა

cars1 = {'cls 63s amg', 'bmw f10 m5 competition', 'audi rs7', 'mercedes c63s amg'}
cars2 = {'cls 63s amg', 'bmw f10 m5 competition', 'bmw m5 f90', 'bmw e39 m5 manual', 'w211 e55 amg'}

x= cars1.difference(cars2)
print(x)