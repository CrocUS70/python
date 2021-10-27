from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абсрактный класс "Геометрическая фигура"
    """
    @abstractmethod
    def square(self):
        """
        Содержит виртуальный метод для вычисления площади фигуры
        """
        pass