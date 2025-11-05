from abc import ABC, abstractmethod

class Drink(ABC):
    size = 0
    price_s = 0
    price_m = 0
    price_l = 0
    choice = 0
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def set_choice(self, choice : int):
        match choice:
            case 1:
                self.choice = self.price_s
                self.size = 1
            case 2:
                self.choice = self.price_m
                self.size = 2
            case 3:
                self.choice = self.price_l
                self.size = 3

class Coffee(Drink):
    def __init__(self, choice : int):
        self.name = "Coffee"
        self.price_s = 1
        self.price_m = 1.5
        self.price_l = 2
        self.set_choice(choice)

    def get_description(self) -> str:
        return "An Coffee "

    def get_price(self) -> float:
        return self.choice

class Thea(Drink):
    def __init__(self, choice : int):
        self.name = "Thea"
        self.price_s = 2
        self.price_m = 2.5
        self.price_l = 3
        self.set_choice(choice)

    def get_description(self) -> str:
        return "An Thea "

    def get_price(self) -> float:
        return self.choice

class Mocha(Drink):
    def __init__(self, choice : int):
        self.name = "Mocha"
        self.price_s = 5
        self.price_m = 6.5
        self.price_l = 7.5
        self.set_choice(choice)

    def get_description(self) -> str:
        return "An Mocha "

    def get_price(self) -> float:
        return self.choice

class Chocolate(Drink):
    def __init__(self, choice : int):
        self.name = "Chocolate"
        self.price_s = 3
        self.price_m = 4
        self.price_l = 5
        self.set_choice(choice)

    def get_description(self) -> str:
        return "An Chocolate "

    def get_price(self) -> float:
        return self.choice


class DrinkDecorator(Drink):
    def __init__(self, drink : Drink):
        self._drink = drink

    def get_price(self):
        return self._drink.get_price()

    def get_description(self):
        return self._drink.get_description()

class CaramelDecorator(DrinkDecorator):
    def get_price(self):
        return self._drink.get_price() + 0.5

    def get_description(self):
        return self._drink.get_description() + "Caramel"

class ChocolateDecorator(DrinkDecorator):
    def get_price(self):
        return self._drink.get_price() + 1

    def get_description(self):
        return self._drink.get_description() + "Chocolate"

class MochaDecorator(DrinkDecorator):
    def get_price(self):
        return self._drink.get_price() + 0.5

    def get_description(self):
        return self._drink.get_description() + "Mocha"


class WhippedCreamDecorator(DrinkDecorator):
    def get_price(self):
        match self._drink.size:
            case 1:
                return self._drink.get_price() + 0.5
            case 2:
                return self._drink.get_price() + 1
            case 3:
                return self._drink.get_price() + 1.5
            case _:
                return self._drink.get_price()

    def get_description(self):
        match self._drink.size:
            case 1:
                return self._drink.get_description() + "Small whipped cream "
            case 2:
                return self._drink.get_description() + "Medium whipped cream"
            case 3:
                return self._drink.get_description() + "Large whipped cream"
            case _:
                return self._drink.get_description() + "Whipped cream"

class Order:
    def __init__(self, drinks : list[DrinkDecorator]):
        self.drinks = drinks

    def get_total_price(self):
        total_price = 0
        for drink in self.drinks:
            print(f"{drink.get_description()} : {drink.get_price()}")
            total_price += drink.get_price()

        return total_price