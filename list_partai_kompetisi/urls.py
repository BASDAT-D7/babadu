from django.urls import path
from list_partai_kompetisi.views import *

app_name = 'list_partai_kompetisi'

urlpatterns = [
    path('', list_partai_kompetisi, name='list_partai_kompetisi'),
]