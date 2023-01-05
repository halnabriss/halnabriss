from mobile import *
from Car import Car

my_mobile =  Mobile("Samsung", "white", 8)

my_car = Car("Mazda", "White", 2 , 1992)

print(my_mobile.color)
print(my_mobile.cpu_cores)
print("My car age is : " + str(my_car.findAge()))
