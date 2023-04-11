from django.urls import path
from MOBILE.views import *

app_name ='MOBILE'

urlpatterns = [
    path('iphone/', iphone, name='iphone'),
    path('android/', android, name='android'),
]
