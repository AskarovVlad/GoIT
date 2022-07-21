# def caching_fibonacci():
#     cache = {}
#
#     def fibonacci(n):
#         if n in cache:
#             return cache[n]
#         else:
#             if not n:
#                 num_fib = 0
#             elif 0 < n <= 2:
#                 num_fib = 1
#             else:
#                 num_fib = fibonacci(n - 1) + fibonacci(n - 2)
#
#             cache[n] = num_fib
#             return num_fib
#
#     return fibonacci

# def discount_price(discount):
#     def dsc_price(price):
#         return price * (1 - discount)
#     return dsc_price


# def format_phone_number(func):
#     def wrapper(*args):
#         return '+38' + func(*args) if len(func(*args)) < 12 else '+' + func(*args)
#
#     return wrapper
#
#
# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone
#
# print(sanitize_phone_number('+38(093)-268-37-95'))

import re


def generator_numbers(string=""):
    lst = re.findall(r"\d+", string)
    for num in lst:
        yield int(num)

n = "The resulting profit was: from the southern possessions $ 100, " \
    "from the northern colonies $500, and the king gave $1000."


def sum_profit(string):
    return sum(generator_numbers(string))

print(sum_profit(n))
