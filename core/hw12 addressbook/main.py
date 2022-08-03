from addressbook import *

FILE_NAME = 'address-book.bin'
BOOK = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return '-Please enter a valid command.' \
                  '\n-If you want to see my feature set input: showcommands'
        except ValueError:
            return '-Please enter a valid name/phone number/date of birth.'
        except IndexError:
            return "-Enter correct data, please."

    return wrapper


@input_error
def hello(*args):
    return "-Hello. How can I help you?" \
           "\n-If you want to see my feature set input: showcommands"


@input_error
def add_record(user_data):
    global BOOK

    return BOOK.add_record(user_data)


@input_error
def show_all(*args):
    if len(BOOK.data) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."
    contact_list = [f"{record}" for record in BOOK.data.values()]
    return '\n'.join(contact_list)


@input_error
def change_phone(user_data):
    if len(user_data) < 3:
        raise IndexError
    name = user_data[0]
    old_phone = user_data[1]
    new_phone = user_data[2]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number'."
    elif name in BOOK:
        BOOK.change_record(name, old_phone, new_phone)
        return BOOK.change_record(name, old_phone, new_phone)
    else:
        raise ValueError


@input_error
def show_phone(user_data):
    if len(user_data) < 1:
        raise IndexError

    name = user_data[0]

    if len(BOOK) == 0:
        return "-Contact book is empty." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number'."
    elif name in BOOK:
        return f"{name}: {BOOK[name].phones}"
    else:
        raise ValueError


@input_error
def show_commands(*args):
    return "-I can such commands as:" \
           "\n add 'name' 'phone' 'birthday' - Adds record a contact with {name} and {phone number} " \
           "and {birthday} (optional parameter) to a book." \
           "\n showall - Show a list of all contacts in the phone book." \
           "\n phone 'name' - Show a contact with {name}." \
           "\n changephone 'name' 'old phone number' 'new phone number' - Changes the old phone number " \
           "to the new phone number {name}." \
           "\n exit or close or . (dot) or goodbye or bye - Terminates program execution."


@input_error
def exit_func(*args):
    return "-Good bye!"


EXIT = (".", "good bye", "goodbye", "close", "exit", 'bye')
COMMANDS = {'hello': hello,
            'add': add_record,
            'showall': show_all,
            'phone': show_phone,
            'changephone': change_phone,
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
        user_command = input('>>> ')
        if user_command.lower().startswith(EXIT):
            print(exit_func())
            break
        print(handler(user_command))


if __name__ == "__main__":
    main()
