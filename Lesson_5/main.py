from calculator import Calculator
from multicalculator import MultiCalculator

# Проверка класса Calculator
calc1 = Calculator(10, 7)

print(calc1)
'''
    Должно вывести:
    
    a = 10
    b = 7
    
    a + b = 17
    a - b = 3
    a * b = 70
    a / b = 1.42
'''

calc1.b = 0
print(calc1.difference())
'''
    Должно вывести:

    10
'''

print(calc1.division())
'''
    Должно вывести:

    На ноль делить нельзя!
'''


# Проверка класса MultiCalculator
calc2 = MultiCalculator(7, 2, 9, 33, 52)

print(calc2)
'''
    Должно вывести:

    7, 2, 9, 33, 52

    Сумма: 103
    Разность: -96
    Произведение: 216216
    Частное: 0,000266
'''