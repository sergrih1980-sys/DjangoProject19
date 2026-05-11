
from django.urls import path
from .views import home  # Локальный  импорт

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
]