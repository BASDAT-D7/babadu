from django.urls import path
from latih_atlet.views import *

app_name = 'latih_atlet'

urlpatterns = [
    path('', latih_atlet, name='latih_atlet'),
    path('submit/', submit_atlet, name='submit_atlet'),
]