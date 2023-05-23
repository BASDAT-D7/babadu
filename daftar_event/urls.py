from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_stadium, name='daftar_event'),
    path('stadium/<str:nama_stadium>/', daftar_event_by_stadium, name='daftar_event_by_stadium'),
    path('stadium/<str:nama_stadium>/event/<int:event_id>/', daftar_kategori, name="daftar_kategori")
]