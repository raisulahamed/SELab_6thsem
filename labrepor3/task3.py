from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape, Drawable):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

class Rectangle(Shape, Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")

def display_shape_info(shape):
    shape.draw()
    print(f"Area: {shape.calculate_area():.2f}\n")

circle = Circle(5)
rectangle = Rectangle(4, 6)

display_shape_info(circle)
display_shape_info(rectangle)
