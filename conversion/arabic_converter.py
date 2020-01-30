"""
    Класс ConverterToArabic проводит конвертацию с римских на арабские числа.

    Принимает строковое значение, проверяет значение на валидность и если значение валидное проводит
    конвертацию.
"""


class ConverterToArabic(str):
    def __init__(self, roman):
        roman = self.check_valid(roman)
        keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        to_arabic = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900',
                     'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        for key in keys:
            if key in roman:
                roman = roman.replace(key, ' {}'.format(to_arabic.get(key)))
        self.arabic = sum(int(num) for num in roman.split())

    def check_valid(self, roman):
        #  метод проверки ввода данных на их валидность
        roman = roman.upper()
        invalid = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM',
                   'A', 'B', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']
        if any(sub in roman for sub in invalid):
            raise ValueError('Такого числа не существует. Вы ввели {}'.format(roman))
        return roman
