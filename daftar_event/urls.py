from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_stadium, name='daftar_event'),
    path('stadium/<str:nama_stadium>/', daftar_event_by_stadium, name='daftar_event_by_stadium'),
    path('stadium/<str:nama_stadium>/event/<str:nama_event>/', daftar_kategori, name="daftar_kategori"),
    path('stadium/<str:nama_stadium>/event/<str:nama_event>/daftar/<str:nama_kategori>', tambah_peserta, name="tambah_peserta")
]