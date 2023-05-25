from django.urls import path
from daftar_sponsor.views import *

app_name = 'daftar_sponsor'

urlpatterns = [
    path('', daftar_sponsor, name='daftar_sponsor'),
    path('list-sponsor/', list_daftar_sponsor, name='list_sponsor'),
]