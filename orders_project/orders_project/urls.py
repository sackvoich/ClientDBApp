from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Админ-панель Django
    path('', include('orders_app.urls')), # Подключаем URL-адреса приложения orders_app
]