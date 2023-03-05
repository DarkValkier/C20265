def int_input(message=''):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Некорректное значение, попробуйте ещё раз.')
        else:
            return result


a = int_input('Введите первое число:')
print(a)
