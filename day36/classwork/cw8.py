# 7)წინა დავალებაში შექმნილი ორი სეტიდან გამოიტანე ელემენტები
# რომლებიც უნიკალურია (ერთერთში თუ არის მაშინ მეორეში აღარ უნდა იყოს)

cars1 = {'cls 63s amg', 'bmw f10 m5 competition', 'audi rs7', 'mercedes c63s amg'}
cars2 = {'cls 63s amg', 'bmw f10 m5 competition', 'bmw m5 f90', 'bmw e39 m5 manual', 'w211 e55 amg'}
x = cars1.symmetric_difference(cars2)
print(x)