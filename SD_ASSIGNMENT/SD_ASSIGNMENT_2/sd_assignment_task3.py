from abc import ABC, abstractmethod

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
        return 3.1416 * self.radius * self.radius
    
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape, Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def draw(self):
        print("Drawing a Rectangle")

# Demonstrating Abstraction and Interface
shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    print(f"Area: {shape.calculate_area()}")
    shape.draw()