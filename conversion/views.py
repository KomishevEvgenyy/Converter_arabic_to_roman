from django.shortcuts import render
from django.http import JsonResponse
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
    template_name = 'conversion/base.html'
    if request.method == 'POST':
        form = ConverterForm(request.POST)
        if form.is_valid():
            data = json.load(request)
            #  Запись данных в переменную которые пришли в request
            if data.isdigit():
                #  проверяем состоит ли строка только из цифр
                number = int(data)
                #  Если True то преобразуем тип str в int
                result = convert(number)
                # Конвертируем полученные данные и результат записываем в переменную
                save = SaveConverter.objects.create(number_converter=number, result_converter=result)
                #  Сохраняем результат в базу данных
                latest_result = {"result": result}

            else:
                result = convert(data)
                # Конвертируем полученные данные и результат записываем в переменную
                save = SaveConverter.objects.create(number_converter=data, result_converter=result)
                #  Сохраняем результат в базу данных
                latest_result = {"result": result}
            return render(request, template_name, latest_result)

    else:
        return render(request, template_name)
