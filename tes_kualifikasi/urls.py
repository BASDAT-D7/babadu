from django.urls import path
from tes_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('', form_data_kualifikasi, name='form_data_kualifikasi'),
    path('list-ujian/', list_ujian_kualifikasi, name='list_ujian'),
    path('pertanyaan/', pertanyaan_kualifikasi, name='pertanyaan_kualifikasi')
]