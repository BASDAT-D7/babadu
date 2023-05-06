from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_atlet, name='dashboard_atlet'),
    path('pelatih/', dashboard_pelatih, name='dashboard_pelatih'),
    path('umpire/', dashboard_umpire, name='dashboard_umpire'),
]