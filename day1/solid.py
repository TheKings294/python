import math
from abc import ABC, abstractmethod

class Car:
    def __init__(self, nom: str, prix: float, option: list[Option]) -> None:
        self.nom = nom
        self.prix = prix
        self.options = option

    def get_nom(self) -> str:
        return self.nom

    def get_prix(self) -> float:
        return self.prix

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def set_prix(self, prix: float) -> None:
        self.prix = prix

    def get_total(self) -> float:
        total = self.prix

        for option in self.options:
            total += option.apply_option(self)

        return total

class Option(ABC):
    @abstractmethod
    def apply_option(self, car: Car) -> None:
        pass

class AbsOption(Option):
    def apply_option(self, car: Car) -> float:
        return  3000

class AutoOption(Option):
    def apply_option(self, car: Car) -> float:
        return car.get_prix() * 0.10

class OuvrantOption(Option):
    def apply_option(self, car: Car) -> float:
        return (car.get_prix() * 0.10) + 5000