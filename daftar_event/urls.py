from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('', daftar_event, name='daftar_event')
]