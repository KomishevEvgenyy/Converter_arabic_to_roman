from django.db import models


class SaveConverter(models.Model):
    number_converter = models.CharField('Конвертация', max_length=30)
    #  поле которое записывает в БД получаемое число
    result_converter = models.CharField('Результат', max_length=30)
    #  поле которое записывает в БД результат конвертации
    ip_address = models.CharField('IP', max_length=256)
    # поле которое записывает в БД IP адрес пользователя который сделал запрос

    def __str__(self):
        return f'{self.number_converter}: {self.result_converter}'

    class Meta:
        verbose_name = 'Сохраненная конвертация'
        verbose_name_plural = 'Сохраненные конвертации'
