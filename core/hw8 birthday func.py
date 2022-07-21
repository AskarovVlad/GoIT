from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(colleagues_birthday_list):
    result_birth_dict = defaultdict(list)

    current_date = datetime.now().date()  # Текущая дата

    current_week = current_date.isocalendar()  # Кортеж: год, № недели от начала года, порядковый номер дня недели (1-7)

    current_week_num = current_week.week  # Номер текущей недели от начала текущего года

    working_days = [1, 2, 3, 4, 5]
    week_days = [6, 7]

    for colleague in colleagues_birthday_list:

        date_of_birth = colleague['birthday'].date()

        birthday_this_year = date_of_birth.replace(current_date.year)  # ДР юзера в текущем году

        full_name_birthday = birthday_this_year.strftime('%A')  # Название дня недели юзера

        birth_week_num = birthday_this_year.isocalendar().week  # Номер текущей недели от начала текущего года юзера

        birth_weekday_num = birthday_this_year.isocalendar().weekday  # Порядковый номер дня недели (1-7) юзера

        if birth_week_num == current_week_num + 1 and birth_weekday_num in working_days:
            result_birth_dict[full_name_birthday].append(colleague['name'])

        elif birth_week_num == current_week_num and birth_weekday_num in week_days:
            result_birth_dict['Monday'].append(colleague['name'])

    return result_birth_dict


def printing_user_name(colleagues_dict):
    list_of_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for day in list_of_weekdays:

        for k, v in colleagues_dict.items():
            if day == k and len(v) > 0:
                print(f'{k}: {", ".join(v)}')


def main():
    users = [{"name": "Alex", "birthday": datetime(day=24, month=6, year=1995)},
             {"name": "Bill", "birthday": datetime(day=2, month=6, year=1994)},
             {"name": "Clon", "birthday": datetime(day=27, month=6, year=1993)},
             {"name": "Derek", "birthday": datetime(day=25, month=6, year=1992)},
             {"name": "Gregor", "birthday": datetime(day=4, month=6, year=1995)},
             {"name": "Giil", "birthday": datetime(day=3, month=6, year=1994)},
             {"name": "Till", "birthday": datetime(day=3, month=6, year=1993)},
             {'name': 'Jacob', 'birthday': datetime(year=1996, month=6, day=30)},
             {'name': 'Logan', 'birthday': datetime(year=1988, month=6, day=2)},
             {'name': 'Matthew', 'birthday': datetime(year=1977, month=6, day=1)},
             {'name': 'Jackson', 'birthday': datetime(year=2000, month=6, day=3)},
             {'name': 'Levi', 'birthday': datetime(year=1996, month=12, day=3)},
             {'name': 'Mateo', 'birthday': datetime(year=1985, month=4, day=4)},
             {'name': 'Theodore', 'birthday': datetime(year=1978, month=5, day=26)},
             {'name': 'Aiden', 'birthday': datetime(year=1979, month=2, day=1)}]

    birthday_colleague_dict = get_birthdays_per_week(users)

    printing_user_name(birthday_colleague_dict)


if __name__ == '__main__':
    main()
