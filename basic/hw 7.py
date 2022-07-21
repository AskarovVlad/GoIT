# from setuptools import setup
#
# d = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
#
#
# def do_setup(args_dict):
#     setup(
#         name=args_dict['name'],
#         version=args_dict["version"],
#         description=args_dict["description"],
#         url=args_dict['url'],
#         author=args_dict['author'],
#         author_email=args_dict['author_email'],
#         license=args_dict['license'],
#         packages=args_dict['packages'])
# def is_integer(s):
#
#     s = s.strip().replace('+', '').replace('-', '')
#     if len(s) == 0:
#         return False
#     if s.isdigit():
#         return True
#     else:
#         return False
# print(is_integer(' -3'))

# def capital_text(s):
#     s1 = s.split()
#     s1[0] = s1[0].capitalize()
#     for i in range(len(s1)):
#         if '.' in s1[i] or '!' in s1[i] or '?' in s1[i]:
#             s1[i+1] = s1[i+1].capitalize()
#     return ' '.join(s1)
# print(capital_text(' asd.  qwe! asd. zxc?  asd, lfropgk. rty, flb! asd? hello world! awesome? yes'))

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     if reverse:
#         char = riddle.rfind(start_letter)
#         return riddle[char:char - word_length:-1] if char != -1 else ''
#     else:
#         char = riddle.find(start_letter)
#         return riddle[char:char + word_length] if char != -1 else ''
#
#
# print(solve_riddle('mi1powerret', 5, 'p'))
# s = 'mi1rewopret'
# print(s[7:2:-1])

def data_preparation(list_data):
    list_data1 = []
    for lst in list_data:
        if len(lst) > 2:
            lst.remove(min(lst))
            lst.remove(max(lst))
            list_data1.extend(lst)
        else:
            list_data1.extend(lst)
    list_data1.sort(reverse=True)
    list_data = list_data1
    return list_data


print(data_preparation([[1, 2, 3, 9, 0], [3, 6, 10, 4], [5, 8, 6, 11]]))
