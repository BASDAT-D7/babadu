from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
  path('', authentication, name='authentication'),
  path('register/', register, name='register'),
  path('register/atlet/', register_atlet, name='register_atlet'),
  path('register/pelatih/', register_pelatih, name='register_pelatih'),
  path('register/umpire/', register_umpire, name='register_umpire'),
  path('login/', login, name='login'),
  path('logout/', logout, name='logout'),
]