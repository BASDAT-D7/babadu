from django.urls import path
from hasil_pertandingan.views import *

app_name = 'hasil_pertandingan'

urlpatterns = [
    path('<str:pertandingan>', hasil_pertandingan, name='hasil_pertandingan'),
]