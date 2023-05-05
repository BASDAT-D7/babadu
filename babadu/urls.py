"""babadu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('dashboard.urls')),
    path('authentication/', include('authentication.urls')),
    path('daftar-atlet', include('daftar_atlet.urls')),
    path('daftar-event/', include('daftar_event.urls')),
    path('daftar-sponsor/', include('daftar_sponsor.urls')),
    path('enrolled-event/', include('enrolled_event.urls')),
    path('hasil-pertandingan/', include('hasil_pertandingan.urls')),
    path('lihat-event/', include('lihat_event.urls')),
    path('list-atlet/', include('list_atlet.urls')),
    path('tes-kualifikasi/', include('tes_kualifikasi.urls')),
]
