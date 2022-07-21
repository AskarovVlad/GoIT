# def total_salary(path):
#     fh = open(path, 'r')
#     total_sum = 0
#     while True:
#         line = fh.readline()
#         lst = [*line.strip().split(',')]
#         total_sum += float(lst[1]) if len(lst) == 2 else 0
#         if not line:
#             fh.close()
#             break
#     return total_sum
# print(total_salary('test.txt'))

# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for departament in employee_list:
#         for employee in departament:
#             fh.write(employee+'\n')
#     else:
#         fh.close()
# write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'test.txt')

# def read_employees_from_file(path):
#     employee_list = []
#     fh = open(path, 'r')
#     while True:
#         line = fh.readline()
#         employee_list.append(line.strip())
#         if not line:
#             fh.close()
#             break
#     return employee_list[:-1]
#
# print(read_employees_from_file('test.txt'))

# def add_employee_to_file(record, path):
#     fh = open(path, 'a')
#     fh.write(record + '\n')
#     fh.close()

# def get_cats_info(path):
#     list_cats_info = []
#     with open(path, 'r') as fd:
#         for info in fd:
#             line = info.strip().split(',')
#             list_cats_info.append({'id': line[0],
#                                    'name': line[1],
#                                    'age': line[2]})
#
#     return list_cats_info
#
# print(get_cats_info('test2.txt'))

# def get_recipe(path, search_id):
#     list_recipes = []
#     search_recipe = None
#     with open(path, 'r') as fd:
#         for info in fd:
#             line = info.strip().split(',')
#             list_recipes.append({'id': line[0],
#                                  'name': line[1],
#                                  'ingredients': line[2:]})
#     for recipe in list_recipes:
#         if search_id == recipe['id']:
#             search_recipe = recipe
#     return search_recipe
#
# print(get_recipe('Recipes.txt', '60b90c1c13067a15887e1ae1'))

# def sanitize_file(source, output):
#     with open(source, 'r') as fd_sourse:
#         source_string = fd_sourse.readlines()
#         for i in range(len(source_string)):
#             clear_str = ''
#             for symbol in source_string[i]:
#                 if not symbol.isdigit():
#                     clear_str += symbol
#             source_string[i] = clear_str
#     with open(output, 'w') as fd_output:
#         for el in source_string:
#             fd_output.write(el)
#
#
# print(sanitize_file('Test.txt', 'Test3.txt'))

