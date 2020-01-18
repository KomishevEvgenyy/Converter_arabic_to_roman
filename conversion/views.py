from django.shortcuts import render
from .models import SaveConverter
from .arabic_converter import ConverterToArabic
from .roman_converter import ConverterToRoman

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def input_numbers(request):
    """
        Метод который будет заисывать входящие данные в базу данных.

        Принимает request.
    """
    num = input('enter you number')
    number = SaveConverter.objects.create(number_converter=num)

    #number = SaveConverter.objects.create(number_converter=request.POST['number'])
    #  запись в базу данных вводимого числа через request.POST
    result = convert(number)
    a = number.create(result_converter=result)
    latest_result = a.order_by('-id')[:1]
    return render(request, 'conversion/base.html')


def convert(number):
    if isinstance(number, int):
        num = ConverterToRoman(number)
        return num.roman
    num = ConverterToArabic(number)
    return num.arabic






