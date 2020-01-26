from django.shortcuts import render
import json

from .models import SaveConverter
from .arabic_converter import ConverterToArabic
from .roman_converter import ConverterToRoman
from .forms import ConverterForm


def convert(number):
    #  Принимает POST запрос и в зависимости от типа данных проводит конвертацию
    if isinstance(number, int):
        #  Проводит конвертацию если получен тип данных int
        num = ConverterToRoman(number)
        return num.roman
    num = ConverterToArabic(number)
    #  Проводит конвертацию если получен тип данных str
    return num.arabic


def input_numbers(request):
    """
        input_numbers принимает POST запрос передает его в функцию convert которая после выполнения записывает данные
        в базу данных
    """
    #  в request прилитает class 'django.core.handlers.wsgi.WSGIRequest'
    print(type(request))
    template_name = 'conversion/base.html'
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            number = request.POST['body']  # как сюда передать результат функции???????????
            #  Запись данных в переменную которые пришли через POST запрос
            result = convert(number)
            # Конвертируем полученные данные и результат записываем в переменную
            save = SaveConverter.objects.create(number_converter=number, result_converter=result)
            #  Сохраняем результат в базу данных
            latest_result = result
            ctx = {'latest_result': latest_result}

            return render(request, template_name, ctx)
    else:
        return render(request, template_name)
