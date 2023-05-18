from django.urls import path
from list_atlet_dilatih.views import *

app_name = 'list_atlet_dilatih'

urlpatterns = [
    path('', list_atlet_dilatih, name='list_atlet_dilatih')
]