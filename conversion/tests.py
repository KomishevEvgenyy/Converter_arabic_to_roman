from django.test import TestCase
# from conversion.views import roman_to_arabic, arabic_to_roman
from conversion.views import convert

number = int(input('введите арабское число'))
print(convert(number))
number = input('введите римское число')
print(convert(number))

# print(roman_to_arabic(int(input('Ввидети арабское число'))))
# print(arabic_to_roman(input('Введитен римское число')))
