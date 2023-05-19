from django.shortcuts import render
from babadu_function.authentication import *

# Create your views here.
@role_required(['UMPIRE'])
def perempat_final(request):
    dummy_perempat_final = {
        'daftar_perempat_final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'B',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
            {
                'id': 2,
                'tim_1': 'C',
                'tim_2': 'D',
                'skor_tim_1': 1,
                'skor_tim_2': 2
            },
            {
                'id': 3,
                'tim_1': 'E',
                'tim_2': 'F',
                'skor_tim_1': 2,
                'skor_tim_2': 1
            },
            {
                'id': 4,
                'tim_1': 'G',
                'tim_2': 'H',
                'skor_tim_1': 2,
                'skor_tim_2': 1
            }
        ]
    }           
    return render(request, 'pertandingan_perempat_final.html', dummy_perempat_final)

@role_required(['UMPIRE'])
def semifinal(request):
    dummy_semifinal = {
        'daftar_perempat_final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'D',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
            {
                'id': 2,
                'tim_1': 'E',
                'tim_2': 'G',
                'skor_tim_1': 1,
                'skor_tim_2': 2
            },
        ]
    }
    return render(request, 'pertandingan_semifinal.html', dummy_semifinal)

@role_required(['UMPIRE'])
def final(request):
    dummy_final = {
        'perebutan_juara_tiga': [
            {
                'id': 2,
                'tim_1': 'D',
                'tim_2': 'E',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
        ],
        'final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'G',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
        ]
    }
    return render(request, 'pertandingan_final_dan_juara_tiga.html', dummy_final)