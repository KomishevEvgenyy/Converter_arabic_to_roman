from django.urls import path
from conversion.views import convert, input_numbers


app_name = 'conversion'
#  привязка url к приложению conversion
urlpatterns = [
     #path('convert/', convert, name='convert'),
     path('input/', input_numbers, name='input')
]
