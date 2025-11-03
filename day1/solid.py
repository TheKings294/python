import math

class Car:
    abs: bool = False
    auto: bool = False
    ouvrant: bool = False
    def __init__(self, nom: str, prix: float) -> None:
        self.nom = nom
        self.prix = prix

    def get_nom(self) -> str:
        return self.nom

    def get_prix(self) -> float:
        return self.prix

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def set_prix(self, prix: float) -> None:
        self.prix = prix

    def add_abs(self) -> None:
        self.abs = True

    def add_ouvrant(self) -> None:
        self.ouvrant = True

    def add_auto(self) -> None:
        self.auto = True

    def get_total(self) -> float:
        total = self.prix
        if self.ouvrant:
            total += self.prix * 0.10
            total += 5000
        elif self.abs:
            total += 3000
        elif self.auto:
            total += self.prix * 0.10

        return total