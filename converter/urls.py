from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('conversion.urls', namespace='conversion')),
]
