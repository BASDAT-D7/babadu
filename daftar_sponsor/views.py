from django.shortcuts import render
from babadu_function.authentication import *

# Create your views here.
def daftar_sponsor(request):
    dummy_daftar_sponsor = {
        'daftar_sponsor': [
            {
                'id': 1,
                'nama_sponsor': 'Yonex',
            },
            {
                'id': 2,
                'nama_sponsor': 'Victor',
            },
            {
                'id': 3,
                'nama_sponsor': 'Li-Ning',
            },
        ]
    }
    return render(request, 'daftar_sponsor.html', dummy_daftar_sponsor)