from abc import ABC, abstractmethod
from enum import Enum, auto


class BrandType(Enum):
    MSI = auto()
    ASUS = auto()
    ACER = auto()
    HP = auto()

class CpuType(Enum):
    I5 = auto()
    I7 = auto()
    I9 = auto()

class RamType(Enum):
    RAM8 = auto()
    RAM16 = auto()

class CardType(Enum):
    GTX1650 = auto()
    GTX1650ti = auto()
    GTX1660ti = auto()
    RTX2060 = auto()

class Laptop:
    def __init__(self, name):
        self.name = name
        self.brand = None
        self.cpu = None
        self.ram = None
        self.card = None
        self.cost = None

    def __str__(self):
       info: str = f"Laptop name: {self.name} \n" \
                   f"{self.brand} \n" \
                   f"{self.cpu} \n" \
                   f"{self.ram} \n" \
                   f"{self.card} \n" \
                   f"Cost: {self.cost} rub"

       return info



class Builder(ABC):

    @abstractmethod
    def add_brand(self) -> None: pass

    @abstractmethod
    def add_cpu(self) -> None: pass

    @abstractmethod
    def add_ram(self) -> None: pass

    @abstractmethod
    def add_card(self) -> None: pass


class MSIGL62LapBuilder(Builder):

    def __init__(self):
        self.laptop = Laptop("MSI GL62")
        self.laptop.cost = 50000

    def add_brand(self) -> None:
        self.laptop.brand = BrandType.MSI

    def add_cpu(self) -> None:
        self.laptop.cpu = CpuType.I5

    def add_ram(self) -> None:
        self.laptop.ram = RamType.RAM8

    def add_card(self) -> None:
        self.laptop.card = CardType.GTX1650

    def get_lap(self) -> Laptop:
        return self.laptop


class ASUSTUFLapBuilder(Builder):

    def __init__(self):
        self.laptop = Laptop("ASUS TUF")
        self.laptop.cost = 100000

    def add_brand(self) -> None:
        self.laptop.brand = BrandType.ASUS

    def add_cpu(self) -> None:
        self.laptop.cpu = CpuType.I7

    def add_ram(self) -> None:
        self.laptop.ram = RamType.RAM16

    def add_card(self) -> None:
        self.laptop.card = CardType.RTX2060

    def get_lap(self) -> Laptop:
        return self.laptop


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_lap(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.add_brand()
        self.builder.add_cpu()
        self.builder.add_ram()
        self.builder.add_card()


def check_cost(name1):
    for it1 in (MSIGL62LapBuilder, ASUSTUFLapBuilder):
        director1 = Director()
        builder1 = it1()
        director1.set_builder(builder1)
        director1.make_lap()
        laptop1 = builder1.get_lap()
        if laptop1.name == name1:
            return laptop1.cost

def sum_cost(x):
    for it1 in (MSIGL62LapBuilder, ASUSTUFLapBuilder):
        director1 = Director()
        builder1 = it1()
        director1.set_builder(builder1)
        director1.make_lap()
        laptop1 = builder1.get_lap()
        x = x + laptop1.cost
    return x


if __name__ == "__main__":
    print("Объекты:")
    director = Director()
    for it in (MSIGL62LapBuilder, ASUSTUFLapBuilder):
        builder = it()
        director.set_builder(builder)
        director.make_lap()
        laptop = builder.get_lap()
        print(laptop)
        print('---------------')
    name = "ASUS TUF"
    print(name, "Cost:", check_cost(name))
    x = 0
    print('sum = ', sum_cost(x))
