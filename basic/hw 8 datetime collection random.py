# from datetime import datetime, timedelta
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)
#
# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0
#
# ts += 100_000
# print(datetime.fromtimestamp(ts))
# print(seventh_day_2020 + delta)
# print(seventh_day_2020 - delta)
# Person = collections.namedtuple('Human', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# print(person)
#
# grouped_words = collections.defaultdict(list)
# print(grouped_words)

# def get_days_from_today(date):
#     return (datetime.now().date() - datetime.strptime(date, '%Y-%m-%d').date()).days
#
#
# print(get_days_from_today('2021-10-09'))
#
#
# def get_days_in_month(month, year):
#     return calendar.monthrange(year, month)[1]
#
#
# print(get_days_in_month(1, 2020))
#
#
# def get_days_in_month_my(month, year):
#     days_in_year = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days_in_leap_year = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         return days_in_leap_year[month]
#     else:
#         return days_in_year[month]
#
#
# print(get_days_in_month(2, 2020))
#
# print(get_days_in_month_my(2, 2020))

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020)
# print(seventh_day_2020.strftime('%A %d %B %Y'))


# def get_str_date(date):
#     date = date.split()
#     date = datetime.strptime(date[0], '%Y-%m-%d')
#     return date.strftime('%A %d %B %Y')
#
# print(get_str_date("2021-05-27 17:08:34.149Z"))


# def get_numbers_ticket(min, max, quantity):
#     if min < 1 or max > 1000 or min > quantity or quantity > max:
#         return []
#     lst = []
#     while quantity:
#         num = random.randrange(min, max)
#         if num in lst:
#             continue
#         lst.append(num)
#         quantity -= 1
#     return lst
#
# print(get_numbers_ticket(10, 15, 5))

# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
#
#
# def get_random_winners(quantity, participant):
#     lst = [*participant.keys()]
#     random.shuffle(lst)
#     return [] if quantity > len(participant) else random.sample(lst, quantity)
#
#
# print(get_random_winners(2, participants))

import collections

# lst = collections.namedtuple('Mark', ['name', 'age', 'weight'])
# print(lst)
#
# named_tuple = lst('Vlad', '26', 173)
# print(named_tuple, named_tuple[0], named_tuple.name)
#
# tpl = lst._make(['Lesia', '25', 168])
#
# print(tpl)
#
# tpl = tpl._replace(name='Lesichka')
# print(tpl)
#
# print(isinstance(tpl, tuple))

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
#
#
# def convert_list(cats):
#     if isinstance(cats[0], tuple):
#         return [cat._asdict() for cat in cats]
#     return [Cat(*d.values()) for d in cats]
#
#
# cats_1 = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# cats_2 = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
#
# print(convert_list(cats_2))

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
#
#
# def get_count_visits_from_ip(ips):
#     return collections.Counter(ips)
#
#
# print(get_count_visits_from_ip(student_marks))

# a = collections.Counter(a=1, b=2, c=3)
# b = collections.Counter(a=2, b=3, c=4)
# print(a, b)
# a.subtract(b)
# print(a)

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = collections.defaultdict(list)
#
# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)
#
# print(grouped_words)

d = collections.deque()
print(d)
d.append('apple')
print(d)
d.extend(['banana', 'orange'])
print(d)
d.appendleft('kiwi')
print(d)
d.popleft()
print(d)
d.insert(2, 'cucumber')
print(d)
