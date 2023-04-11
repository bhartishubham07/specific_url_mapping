from django.urls import path
from LAPTOP.views import *

app_name = 'LAPTOP'

urlpatterns = [
    path('asus/', asus, name='asus'),
    path('acer/', acer, name='acer'),
]
