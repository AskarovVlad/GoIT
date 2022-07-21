import shutil

archive_name = shutil.make_archive('testbackup', 'zip', r'C:\Users\DESKTOP-65L32PF\Desktop\ноут')
shutil.unpack_archive(archive_name, r'C:\Users\DESKTOP-65L32PF\Desktop\Новая папка')
for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))
