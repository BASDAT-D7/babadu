from django.urls import path
from auth.views import register, login, logout

app_name = 'auth'

urlpatterns = [
  path('register/', register, name='register'),
  path('login/', login, name='login'),
  path('logout/', logout, name='logout'),
]