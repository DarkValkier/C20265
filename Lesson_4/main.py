a = 6
b = 2

try:
    print(f'{a} / {b} = {a / b}')

except ZeroDivisionError:
    print('Делить на ноль нельзя!')
except NameError as error:
    print(f'Использовано несуществующее название: {error}')
except Exception as error:
    print(type(error), error)
else:
    print('Исключений не было!')
finally:
    print('Этот блок сработает в любом случае')


print('Конец программы')