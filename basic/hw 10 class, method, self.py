class Counter:

    def start_from(self, start=0):
        self.start_count = start

    def increment(self):
        self.start_count += 1

    def display(self):
        value = self.start_count
        print(f"Текущее значение счетчика = {value}")

    def reset(self):
        self.start_count = 0


# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display()
# c1.increment()
# c1.display()
# c1.reset()
# c1.display()
#
# c2 = Counter()
# c2.start_from(3)
# c2.display()
# c2.increment()
# c2.display()


class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, exemplar):
        if isinstance(exemplar, Point):
            return ((self.x - exemplar.x) ** 2 + (self.y - exemplar.y) ** 2) ** 0.5
        else:
            print("Передана не точка")


# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2)
# p1.get_distance(10)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#
#     def say(self):
#         pass
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#
# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def info(self):
#         return {'name': self.name, 'age': self.age, "address": self.address}
#
#
# class Dog(Animal):
#
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)
#
#     def say(self):
#         return "Woof"
#
#     def who_is_owner(self):
#         return self.owner.info()
#
# owner = Owner("Sherlock", 24, "London, 221B Baker Street")
# dog = Dog("Simon", 10, "british", owner)
# print(dog.who_is_owner())

# from collections import UserString
#
#
# class NumberString(UserString):
#     def number_count(self):
#         sum_val = 0
#         for value in self:
#             if value.isdigit():
#                 sum_val += 1
#         return sum_val
#
# d = NumberString('123gvsp23')
# print(d.number_count())

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": self.current_id,
                              "name": name,
                              "phone": phone,
                              "email": email,
                              "favorite": favorite,
                              }
                             )
        self.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        value = self.get_contact_by_id(id)
        if value:
            self.list_contacts().remove(value)

# c1 = Contacts()
# c1.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', False)
# c1.add_contacts('WWWWWWWWWWWe', '(692) 802-2949', 'est@utquamvel.net', True)
# c1.add_contacts('QQQQQQQQ', '(692) 802-2949', 'est@utquamvel.net', False)
# print(c1.list_contacts())
# print(c1.get_contact_by_id(1))
# c1.remove_contacts(5)
# print(c1.list_contacts())
