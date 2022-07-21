# class Session:
#     def __init__(self, addr, port=8080):
#         self.connected = True
#         self.addr = addr
#         self.port = port
#
#     def __enter__(self):
#         print(f"connected to {self.addr}:{self.port}")
#         return self
#
#     def __exit__(self, exception_type, exception_value, traceback):
#         self.connected = False
#         if exception_type is not None:
#             print("Some error!")
#         else:
#             print("No problem")


# class Point:
#     def __init__(self, x, y):
#         self.get_x = x
#         self.get_y = y
#
#     @property
#     def get_x(self):
#         return self.__x
#
#     @get_x.setter
#     def get_x(self, other):
#         self.__x = other
#
#     @property
#     def get_y(self):
#         return self.__y
#
#     @get_y.setter
#     def get_y(self, other):
#         self.__y = other

# p1 = Point(1, 2)
# print(p1.get_x)
# print(p1.get_y)
#
# p1.get_x = 10
# p1.get_y = 20
# print(p1.get_x)
# print(p1.get_y)

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y


# p1 = Point("1", 2)
# print(p1.__dict__)
# print(p1.x, p1.y)


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __add__(self, vector):
        return Vector(Point(self.coordinates.x + vector[0], self.coordinates.y + vector[1]))

    def __sub__(self, vector):

        return Vector(Point(self.coordinates.x - vector[0], self.coordinates.y - vector[1]))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

# В целях упрощения сравнивать экземпляры класса Vector будем только по их длине,
    # используя метод len, не учитывая направление векторов.
    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    # def __ne__(self, vector):

    def __lt__(self, vector):
        return self.len() < vector.len()

    # def __gt__(self, vector):

    def __le__(self, vector):
        return self.len() <= vector.len()

    # def __ge__(self, vector):


# v1 = Vector(Point(1, 2))
# print(v1.coordinates.x)
# print(v1)
# v2 = Vector(Point(3, 4))
# v3 = v1 + v2
# print(v3)

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))
print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True

