from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


class Record:

    def __init__(self, name: Name, phone: Phone = None, email: Email = None):
        self.name = name
        self.phones = list()
        self.email = list()

        if phone:
            self.phones.append(phone)

        if email:
            self.email.append(email)

    def __str__(self):
        return f"{self.name} {self.phones} {self.email}"

    def __repr__(self):
        return f"{self.name} {self.phones} {self.email}"

    def add_phone(self, phone: Phone):
        return self.phones.append(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone in self.phones:
            return self.phones.remove(old_phone)
        return self.phones.append(new_phone)

    def remove_phone(self, phone: Phone):
        if phone in self.phones:
            return self.phones.remove(phone)


class AddressBook(UserDict):

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"

    def add_record(self, record):
        if record.name.value not in self.data:
            return self.data.update({record.name.value: record})
        else:
            return f"""Name '{record.name.value}' already exist in address book."""

    def change_record(self, old_record: Record, new_record: Record):
        return self.data.update({old_record.name.value: new_record})

    def remove_record(self, record: Record):
        return self.data.pop(record.name.value, "Record not found")

    def find_record(self, value: Name):
        return self.data.get(value, "Record not found")


name_1 = Name('Vlad')
phone_1 = Phone('111')

r = Record(name_1, phone_1, "vlad@gmail.com")
print(1, r.name, r.phones, r.email)

a = AddressBook()
print(2, f"AddressBook - {a.data}")

a.add_record(r)
print(3, f"AddressBook - {a.data}")
print(4, a.data)

phone_2 = Phone('222')
r.add_phone(phone_2)
print(5, r)
print(6, a)

r.add_phone('123123')
print(7, r)
print(8, a)
print(9, phone_1)

phone_3 = Phone('333')
print(10, r)
r.change_phone(phone_1, phone_3)
print(11, r)
print(12, a["Vlad"].phones)

a['Vlad'].remove_phone(phone_3)
print(13, a['Vlad'].phones)

r.change_phone(Phone('1111'), Phone('5555'))
print(14, a['Vlad'].phones)
a.add_record(Record(Name('Lesia'), Phone("+38093"), Email("lesia@gmail.com")))
print(15, a)
a.add_record(Record(Name("Lesia")))
print(16, a.find_record('mgeg'))

a.remove_record(Record(Name('Vlad')))
print(17, a)
a.remove_record(Record(Name('Vlad')))
print(18, a)
