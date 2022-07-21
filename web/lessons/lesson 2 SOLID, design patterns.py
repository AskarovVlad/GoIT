# Single responsibility
class PersonAddress:
    def __init__(self, zips, city, street):
        self.zips = zips
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zips}, {self.city}, {self.street}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address.value_of()


person = Person('Alexander', PersonAddress('36007', 'Poltava', 'European, 28'))
print(person.get_address())

# Open-closed
from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


def total_area(shapes):
    total_sum = 0
    for el in shapes:
        total_sum += el.area_of()
    return total_sum


shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
area = total_area(shapes)
print(area)

# Liskov substitution
from enum import Enum


class SideType(Enum):
    TYPE_WIDTH = 'width'
    TYPE_HEIGHT = 'height'


class Shape:
    def set_side(self, size, side):
        pass

    def area_of(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_side(self, size, side):
        if SideType.TYPE_WIDTH == side:
            self.width = size
        if SideType.TYPE_HEIGHT == side:
            self.height = size

    def set_width(self, width):
        self.set_side(width, SideType.TYPE_WIDTH)

    def set_height(self, height):
        self.set_side(height, SideType.TYPE_HEIGHT)

    def area_of(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.edge = size

    def set_side(self, size, side=None):
        self.edge = size

    def set_width(self, width):
        self.set_side(width)

    def area_of(self):
        return self.edge ** 2


square = Square(10)
rect = Rect(5, 10)

# Interface segregation


class CodeProducer:
    def write_code(self):
        pass


class PizzaConsumer:
    def eat_pizza(self, slice_count):
        pass


class OfficeProgrammer(CodeProducer, PizzaConsumer):
    def __init__(self, name):
        self.name = name

    def eat_pizza(self, slice_count):
        print(f'{self.name} eat {slice_count} slice pizza!')

    def write_code(self):
        print(f'{self.name} write code!')


class RemoteProgrammer(CodeProducer):
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f'{self.name} write code!')

# Dependency inversion


