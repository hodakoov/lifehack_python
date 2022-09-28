'''
Программа переименовывает расширения файла в ".focus", даже если у файла нет расширения
+ небольшая корректировка имени
'''

import os

DIR = r'C:\projects python\lifehack\1RenameFiles\files'


def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)

    os.rename(old_file, new_file)


def get_valid_name(name):

    symbol_space = ['-', '_']
    symbol_not_space = ['(1)', '[', ']']

    for s in symbol_space:
        name = name.replace(s, ' ')

    for s in symbol_not_space:
        name = name.replace(s, '')

    name = name.replace(' .', '.')
    name = name[::-1].split('.', 1)
    result = name[1:]

    if not len(result):
        result = name[0][::-1] + '.focus'
    else:
        result = result[0][::-1] + '.focus'

    return result


if __name__ == '__main__':
    rename_files(DIR)