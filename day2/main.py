from car import *
from coffee import *

#car = Car("Porsche", 150000, [AbsOption(), AutoOption()])

#print(car.get_total())

coffee = Coffee(1)
coffee = CaramelDecorator(coffee)

thea = Thea(3)

chocolate = Chocolate(2)
chocolate = WhippedCreamDecorator(chocolate)

order = Order([coffee, thea, chocolate])

print(f"Total : {order.get_total_price()}")