from calculator import Calculator


class MultiCalculator(Calculator):
    numbers = []

    def __init__(self, *args):
        Calculator.__init__(self)
        for argument in args:
            self.numbers.append(argument)

    def __str__(self):
        '''
        Список чисел (self.numbers)

        Сумма чисел
        Разность чисел
        Произведение чисел
        Частное чисел
        '''
        return str(self.numbers)

    def sum(self):
        sum = 0
        for num in self.numbers:
            sum += num
        return sum

    def subtract(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result
