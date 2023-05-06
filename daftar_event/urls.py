from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_stadium, name='daftar_event'),
    path('stadium/<int:id>/', daftar_event_by_stadium, name='daftar_event_by_stadium'),
    path('stadium/<int:id>/kategori/', daftar_kategori, name="daftar_kategori")
]