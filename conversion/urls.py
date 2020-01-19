from django.urls import path
from conversion.views import input_numbers


app_name = 'conversion'
#  привязка url к приложению conversion
urlpatterns = [
     path('input/', input_numbers, name='input'),
]
