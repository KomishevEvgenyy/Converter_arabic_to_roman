from django.urls import path
from conversion.views import convert


app_name = 'conversion'
#  привязка url к приложению conversion
urlpatterns = [
     path('', convert, name='convert'),
]
