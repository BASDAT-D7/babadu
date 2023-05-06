from django.urls import path
from tes_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('', form_data_kualifikasi, name='form_data_kualifikasi'),
    path('pertanyaan/', pertanyaan_kualifikasi, name='pertanyaan_kualifikasi')
]