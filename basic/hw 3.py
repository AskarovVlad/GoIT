# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         if ch.isupper():
#             pos = ord(ch) - ord('A')
#             pos = (pos + offset) % 26
#             new_char = chr(pos + ord("A"))
#             encoded_message += new_char
#         else:
#             pos = ord(ch) - ord('a')
#             pos = (pos + offset) % 26
#             new_char = chr(pos + ord("a"))
#             encoded_message += new_char
#     else:
#         encoded_message += ch
# print(encoded_message)
# print(ord('a'), ord('A'))
# a = 'Aa'
# for el in a:
#     if el.isupper():
#         print(el)
# x = 50
# def get_fullname(first_name, last_name, middle_name=False):
#     if middle_name:
#         return f'{first_name} {middle_name} {last_name}'
#     else:
#         return f'{first_name} {last_name}'
# print(get_fullname('Vlad', 'Askarov', 'Sergeevich'))

# def first(size, *args):
#     return size + len(args)
#
#
# def second(size, **kwargs):
#     return size + len(kwargs)
#
#
# print(first(5, "first", "second", "third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))
#
#
# def cost_delivery(quantity, *numbers, discount=0):
#     sum = 0
#     if quantity > 0:
#         sum = (5 + 2 * (quantity - 1)) - (5 + 2 * (quantity - 1)) * discount
#
#     return sum
#
#
# print(cost_delivery(2, 2, 3, discount=0.5))
# def factorial(x):
#      if x < 2:
#         return 1
#      else:
#         return x * factorial(x - 1)
#
#
# def number_of_groups(n, k):
#     lst = factorial(n) / (factorial(n-k) * factorial(k))
#     return lst
# print(number_of_groups(50, 7))
# def prepare_data(data):
#     data.remove(min(data))
#     data.remove(max(data))
#     data.sort()
#     return data
#
# print(prepare_data([1, 2, 3]))
# def format_ingredients(items):
#     s = ''
#     if len(items) == 0:
#         return ''
#     elif len(items) == 1:
#         return items[0]
#     elif len(items) == 2:
#         return items[0] + ' и ' + items[1]
#     else:
#         for i in range(len(items)-2):
#             s = s + items[i] + ', '
#         return s + items[-2] + ' и ' + items[-1]
# print(format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']))
# print('яйца 2шт, сахар 1 л., соль 1 чл. и уксус')
# def lookup_key(data, value):
#     lst = []
#     for k, v in data.items():
#         if v == value:
#             lst.append(k)
#     return lst
# print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))
# def split_list(grade):
#     grade.sort()
#     t = ([], [])
#     if len(grade) < 1:
#         return t
#     elif len(grade) % 2 != 0:
#         for i in range(len(grade) // 2 + 1):
#             t[0].append(grade[i])
#         for j in range(len(grade) // 2 + 1, len(grade)):
#             t[1].append(grade[j])
#         return t
#     else:
#         for i in range(len(grade) // 2):
#             t[0].append(grade[i])
#         for j in range(len(grade) // 2, len(grade)):
#             t[1].append(grade[j])
#         return t
#
# print(split_list([1, 2, 3, 4, 5]))
# print(split_list([]))
# print(split_list([1, 2, 3, 4]))
