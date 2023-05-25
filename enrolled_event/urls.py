from django.urls import path
from enrolled_event.views import *

app_name = 'enrolled_event'

urlpatterns = [
    path('', enrolled_event, name='enrolled_event'),
    path('partai-kompetisi/', enrolled_partai, name='enrolled_partai'),


]