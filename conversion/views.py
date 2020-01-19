from django.shortcuts import render

from .models import SaveConverter
from .arabic_converter import ConverterToArabic
from .roman_converter import ConverterToRoman


from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def convert(number):
    #  принимает POST запрос и в зависимости от типа данных проводит конвертацию
    if isinstance(number, int):
        #  проводит конвертацию если получен тип данных int
        num = ConverterToRoman(number)
        return num.roman
    num = ConverterToArabic(number)
    #  проводит конвертацию если получен тип данных str
    return num.arabic


def input_numbers(request):
    """
        Метод который будет записывать входящие данные в базу данных, а так же результат конвертации.

        Принимает request который через метод POST записывает в базу входящие данные
    """
    if request.method == 'POST':
        number, number2 = SaveConverter.objects.create(number_converter=request.POST['num']), request.POST['num']
        #  запись данных которые пришли через POST запрос
        result = convert(number2)
        b = SaveConverter.objects.update(result_converter=result)
        #  запись результат конвертации в базу данных
    latest_result = SaveConverter.objects.order_by('result_converter')

    return render(request, 'conversion/base.html', {'latest_result': latest_result})
