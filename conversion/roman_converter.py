"""
    Класс ConverterToRoman проводит конвертацию с арабских на римские числа.

    Принимает значение типа int, проверяет корректность ввода данных (число должно быть от 1 до 3999). Если данные
    введены верно, проводит конвертацию.
"""


class ConverterToRoman(int):
    def __new__(cls, number):
        if number > 3999:
            raise ValueError('Values over 3999 are not allowed: {}'.format(number))
        if number < 0:
            raise ValueError('Negative values are not allowed: {}'.format(number))
        return super().__new__(cls, number)

    def __init__(self, number):
        to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                    30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                    90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                    600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                    2000: 'MM', 3000: 'MMM'}
        self.roman = ''.join([to_roman.get(num) for num in self][::-1])

    def __iter__(self):
        number = self.__str__()
        count = 1
        for digit in number[::-1]:
            if digit != '0':
                yield int(digit) * count
            count *= 10
