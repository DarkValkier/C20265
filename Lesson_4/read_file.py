def open_file():
    file_name = input('Введите название файла: ')
    file = open(file_name, 'r')
    return file


file = open_file()

print('\nСодержимое файла:')
for line in file.readlines():
    print(line.strip('\n'))

file.close()