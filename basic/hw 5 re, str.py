import re

print('{0:+}, {0:-}, {0:d}, {1:x}, {1:b}, {1:<5}, {1:*^10}'.format(5, 15))


def real_len(text):
    return len(re.findall('[^\\n\\f\\r\\t\\v]', text))


s = 'Alex\nKdfe23\t\f\v.\r+380932683795jgjg25hl;,t,ph46'
print(real_len(s))
print(len(re.findall(r'\d{2}\b', s)))
print(re.findall(r'\d\d\b', s))
print(re.search(r'\d{2}\b', s))
match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
print(match[0] if match else 'Not found')
test_str = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', test_str)
print(result)


# print(real_len(s))
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
#
#
# def find_articles(key, letter_case=False):
#     new_list = []
#     for el in articles_dict:
#         lst = el['title'] + el['author']
#         if not letter_case:
#             if key in lst or key.upper() in lst or key.lower() in lst or key.capitalize() in lst:
#                 new_list.append(el)
#             else:
#                 continue
#         else:
#             if key in lst:
#                 new_list.append(el)
#             else:
#                 continue
#     return new_list
#
#
# # print(find_articles("Silver"))
# def sanitize_phone_number(phones):
#     clear_phone = ''
#     for char in phones:
#         if char.isdigit():
#             clear_phone += char
#     return clear_phone
#
#
# print(sanitize_phone_number("     0503451234"))
#
#
# def is_check_name(fullname, first_name):
#     f = fullname.removeprefix(first_name)
#     if f == fullname:
#         return False
#     else:
#         return True
#
#
# print(is_check_name('Askarov Vlad', 'Ask'))
#
# country_code = {'+81': 'JP', '+65': 'SG', '+886': 'TW', '+380': 'UA'}
# sort_dict_phones = {}
#
#
# def get_phone_numbers_for_countries(list_phones):
#     for i in range(len(list_phones)):
#         list_phones[i] = sanitize_phone_number(list_phones[i])
#     for phon in list_phones:
#         for code in country_code:
#             if phon[:2] == code[1:] or phon[:3] == code[1:]:
#                 if country_code[code] in sort_dict_phones:
#                     sort_dict_phones[country_code[code]].append(phon)
#                     break
#                 else:
#                     sort_dict_phones[country_code[code]] = [phon]
#                     break
#         else:
#             if 'UA' not in sort_dict_phones:
#                 sort_dict_phones['UA'] = [phon]
#             else:
#                 sort_dict_phones["UA"].append(phon)
#     return sort_dict_phones
#
#
# lst_ph = ['380998759405', '818765347', '8867658976', '657658976', '999999999']
#
# print(get_phone_numbers_for_countries(lst_ph))
#
# for k in sort_dict_phones:
#     print('{}: {}'.format(k, sort_dict_phones[k]))
