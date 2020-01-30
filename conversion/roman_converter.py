"""
    Класс ConverterToRoman проводит конвертацию с арабских на римские числа.

    Принимает значение типа int, проверяет корректность ввода данных (число должно быть от 1 до 3999). Если данные
    введены верно, проводит конвертацию.
"""


class ConverterToRoman(int):
    def __init__(self, number):
        number = self.check_valid(number)
        roman_value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_char_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        for i in range(len(roman_value_list)):
            while number >= roman_value_list[i]:
                number -= roman_value_list[i]
                res += roman_char_list[i]
                self.roman = res

    def check_valid(self, number):
        #  проверка валидности числа
        if number > 3999 or number < 0:
            raise Exception('Число введено не верно. Введите число от 1 до 3999: {}'.format(number))
        else:
            return number
