# import json
# import pickle
# # import copy
#
# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}, 'asd': True}
#
# byte_string = json.dumps(some_data)
# unpacked_JSON = json.loads(byte_string)
#
# print(some_data)
# print(byte_string)
# print(unpacked_JSON)
# print(type(unpacked_JSON))
# unpacked_JSON['vlad'] = 'lesia'
# print(unpacked_JSON)

# print(unpacked_JSON is some_data)    # False
# print(unpacked_JSON == some_data)    # False
#
# print(unpacked_JSON['key'] == some_data['key'])     # True
# print(unpacked_JSON['a'] == some_data['a'])         # True
# print(unpacked_JSON['2'] == some_data[2])           # True
# print(unpacked_JSON['tuple'] == [5, 6])             # True
# print('------------------------------------------------')
# print('Pickle is binary serialization, dump(load read from file) saved in file, dumps(loads) saved in variable and send ')
#
# byte_string_pickle = pickle.dumps(some_data)


# unpacked_PICKLE = pickle.loads(byte_string_pickle)
#
# print(unpacked_PICKLE is some_data)    # False
# print(unpacked_PICKLE == some_data)    # True
# print('unpacked_PICKLE == some_data, но unpacked_JSON != some_data потому, что в JSON: кортежи при распаковке')
# print('становятся списками; ключи словаря, если они были числами, становятся строками.')

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'wb') as fh:
#         pickle.dump(contacts, fh)
#
# def read_contacts_from_file(filename):
#     with open(filename, 'rb') as fh:
#         contacts = pickle.load(fh)
#     return contacts

#
#
import csv
# with open('1eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#
#
# with open('1eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))


contacts = [
    {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
    {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False},
    {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True},
    {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False},
    {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]


# with open('1enames.csv', 'w', newline='') as fh:
#     field_names = ['name', 'email', 'phone', 'favorite']
#     writer = csv.DictWriter(fh, fieldnames=field_names)
#     writer.writeheader()
#     for contact in contacts:
#         writer.writerow({'name': contact['name'], 'email': contact['email'],
#                          'phone': contact['phone'], 'favorite': contact['favorite']})
#
# contacts1 = []
# with open('1enames.csv', 'r', newline='') as fh:
#
#     for row in csv.DictReader(fh):
#         row['favorite'] = eval(row['favorite'])
#         contacts1.append(row)
# print(contacts1)
# print('-------------------')
# import json
#
#
# def write_contacts_to_file(filename, contacts):
#     contacts = {'contacts': contacts}
#     with open(filename, 'w') as fh:
#         json.dump(contacts, fh)
#
#
# def read_contacts_from_file(filename):
#     with open(filename, 'r') as fh:
#         contacts = json.load(fh)
#     return contacts['contacts']
#
# write_contacts_to_file('1eggsJSON.json', some_data)
# read_contacts_from_file("1eggsJSON.json")

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite
#
#
# class Contacts:
#
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.count_save = 0
#         self.is_unpacking = False
#
#     def save_to_file(self):
#         with open(self.filename, 'wb') as fh:
#             pickle.dump(self, fh)
#
#     def read_from_file(self):
#         with open(self.filename, 'rb') as fh:
#             content = pickle.load(fh)
#         return content
#
#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes['count_save'] += 1
#         attributes['fh'] = None
#         return attributes
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.is_unpacking = True
#
#
# contacts_in = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# persons = Contacts("1user_class.dat", contacts_in)
# print(persons)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(person_from_file)
# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

# persons = Contacts("1user_class.dat", contacts_in)
# persons.save_to_file()
# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()
#
# print(persons.count_save)  # 0
# print(first.count_save)  # 1
# print(second.count_save)  # 2
# print(third.count_save)  # 3
# print(persons.is_unpacking)
# print(first.is_unpacking)
#
#
# def copy_class_person(person):
#     return copy.copy(person)

import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        copy_obj.name = copy.copy(self.name)
        copy_obj.email = copy.copy(self.email)
        copy_obj.phone = copy.copy(self.phone)
        copy_obj.favorite = copy.copy(self.favorite)
        return copy_obj


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        copy_obj.filename = copy.copy(self.filename)
        copy_obj.contacts = copy.copy(self.contacts)
        copy_obj.is_unpacking = copy.copy(self.is_unpacking)
        copy_obj.count_save = copy.copy(self.count_save)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = copy.deepcopy(self.filename)
        copy_obj.contacts = copy.deepcopy(self.contacts)
        copy_obj.is_unpacking = copy.deepcopy(self.is_unpacking)
        copy_obj.count_save = copy.deepcopy(self.count_save)
        return copy_obj

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
some_data_1 = [1, 2, 3]
data = [some_data, some_data_1]
with open('1pickle.txt', 'wb') as fh:
    pickle.dump(data, fh)
