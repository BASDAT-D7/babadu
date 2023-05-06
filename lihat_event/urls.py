from django.urls import path
from lihat_event.views import *

app_name = 'lihat_event'

urlpatterns = [
    path('', lihat_event, name='lihat_event'),
]