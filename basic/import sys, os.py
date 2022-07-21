import os
import sys

directory = sys.argv[0]  # расположение файла включая название фала
print(directory)
print(sys.path)  # все пдиректории в которых пайтон ищет файл
print('---------------------------')
print(os.getcwd())  # расположение файла, директория
os.chdir(r'C:\Users\DESKTOP-65L32PF\Desktop\all-my-projects-are-in-python\Hillel')  # переход на другую директорию
print(os.getcwd())
print(os.path.exists("D:/test.txt"))  # Проверка существования пути
# images = ['JPEG', 'PNG', 'JPG', 'SVG']
# video = ['AVI', 'MP4', 'MOV', 'MKV']
# documens = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
# audio = ['MP3', 'OGG', 'WAV', 'AMR']
# archives = ['ZIP', 'GZ', 'TAR']
#
# def sort_directory(path):
#     with open(r'C:\Users\DESKTOP-65L32PF\Desktop\Новая папка', 'r') as fd:
#         for file_name in fd:
#             print(file_name, end=' ')
#
# print(sort_directory(r'C:\Users\DESKTOP-65L32PF\Desktop\Новая папка'))
s = '3800932683795'
s1 = s[-10:]
print(s, s1)
print(s1)
a = [1, 22, 13, 46, 35, 6, 7, 8]
a.sort(reverse=True)
print(a)
