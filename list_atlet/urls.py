from django.urls import path
from list_atlet.views import *

app_name = 'list_atlet'

urlpatterns = [
    path('', list_atlet, name='list_atlet')
]