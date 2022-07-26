# import pickle
from addressbook import *


FILE_NAME = 'address-book.bin'
BOOK = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except KeyError:
            print('\n-Please enter a valid command.'
                  '\n If you want to see my feature set input: showcommands')
        except ValueError:
            print('\n-Please enter a valid name/phone number.')
        except IndexError:
            print("-Enter correct data, please.")

    return wrapper


@input_error
def hello(*args):
    print("-Hello. How can I help you."
          "\n If you want to see my feature set input: showcommands")


@input_error
def contact_add(user_data):
    global BOOK
    return BOOK.add_record(*user_data)


@input_error
def show_all(*args):
    if len(BOOK.data) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    return BOOK.iterator(args)


@input_error
def change_contact(user_data):
    name = user_data[0]
    contact = user_data[1]

    if len(BOOK) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    elif name in BOOK:
        old_num = BOOK[name]
        BOOK[name] = contact
        print(f"-You have successfully changed contact {name} with phone number '{old_num}' at '{contact}'")
    else:
        raise ValueError


@input_error
def show_phone(user_data):
    name = user_data[0]

    if len(BOOK) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    elif name in BOOK:
        print(name, BOOK[name])
    else:
        raise ValueError


@input_error
def show_commands(*args):
    print("-I can such commands as:"
          "\n add 'name' 'phone' - Adds a contact {name} and {phone number} to a book"
          "\n showall - Show a list of all contacts in the phone book"
          "\n phone 'name' - Show a contact with name {name}"
          "\n change 'name' 'phone number' - Changes phone number {name}")


@input_error
def exit_func(*args):
    print("-Good bye!")


EXIT = (".", "good bye", "goodbye", "close", "exit", 'bye')
COMMANDS = {'hello': hello,
            'add': contact_add,
            'showall': show_all,
            'phone': show_phone,
            'change': change_contact,
            'showcommands': show_commands}


@input_error
def handler(user_input):

    if not user_input.lower().startswith(tuple(COMMANDS.keys())):
        raise KeyError
    else:
        command = user_input.split()[0].lower()
        data = user_input.split()[1:]
        return COMMANDS[command](data)


def main():
    print("""Hello. I am CLI (Command Line Interface) or your personal bot helper.\
    \nI can work with phone book and calendar.\
    \nIf you want to see my feature set input: showcommands""")

    while True:
        user_command = input('>>> ').lower()
        if user_command.startswith(EXIT):
            exit_func()
            break
        handler(user_command)

if __name__ == "__main__":
    main()

