from django.shortcuts import render
from babadu_function.authentication import *

# Create your views here.
@role_required(['ATLET'])
def enrolled_event(request):
    dummy_enrolled_event = {
        'enrolled_events': [
            {
                'id': 1,
                'nama_event': 'Badminton Open',
                'stadium': 'Gelora Bung Karno',
                'stadium_id': '1',
                'hadiah': 'Rp 5.000.000',
                'kategori_superseries': 'S200',
                'kategori_spesialisasi': 'Ganda Putra',
                'tanggal_mulai': '03-04-2023',
                'tanggal_selesai': '27-04-2023',
                'kapasitas_terisi': 3,
                'kapasitas_total': 8
            },
            {
                'id': 2,
                'nama_event': 'Bali Open',
                'stadium': 'Senayan',
                'stadium_id': '2',
                'hadiah': 'Rp 4.000.000',
                'kategori_superseries': 'S100',
                'kategori_spesialisasi': 'Ganda Campuran',
                'tanggal_mulai': '12-05-2023',
                'tanggal_selesai': '18-05-2023',
                'kapasitas_terisi': 6,
                'kapasitas_total': 10
            },
            {
                'id': 3,
                'nama_event': 'Surabaya Championship',
                'stadium': 'Surabaya',
                'stadium_id': '3',
                'hadiah': 'Rp 7.000.000',
                'kategori_superseries': 'S150',
                'kategori_spesialisasi': 'Tunggal Putra',
                'tanggal_mulai': '01-06-2023',
                'tanggal_selesai': '05-06-2023',
                'kapasitas_terisi': 4,
                'kapasitas_total': 6
            }
        ]
    }
    return render(request, 'enrolled_event.html', dummy_enrolled_event)