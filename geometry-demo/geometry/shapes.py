from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, side: float):
        if side < 0:
            raise ValueError("Side length must be non-negative")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)