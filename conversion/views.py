from django.shortcuts import render
from conversion.models import SaveConverter
from django.http import HttpResponseRedirect
from django.urls import reverse

from .arabic_converter import ConverterToArabic
from .roman_converter import ConverterToRoman


def convert(number):
    if isinstance(number, int):
        num = ConverterToRoman(number)
        return num.roman
    num = ConverterToArabic(number)
    return num.arabic


def input_numbers(request, number):
    num = SaveConverter.objects.create(number_convert=request.POST['input'])
    #  запись в базу данных вводимого числа
    return HttpResponseRedirect(reverse('conversion.base'))



