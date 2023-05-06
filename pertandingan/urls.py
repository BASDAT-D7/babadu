from django.urls import path
from pertandingan.views import *

app_name = 'pertandingan'

urlpatterns = [
    path('', perempat_final, name='perempat_final'),
    path('semifinal/', semifinal, name='semifinal'),
    path('final/', final, name='final')
]