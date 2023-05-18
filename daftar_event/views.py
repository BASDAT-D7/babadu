from django.shortcuts import render
from babadu_function.general import *

# Create your views here.
def daftar_stadium(request):
    # result = query_result(f"SELECT * FROM stadium WHERE")
    # print(result)
    dummy_daftar_stadium = {
        'daftar_stadium': [
            {
                'id': 1,
                'nama_stadium': 'Gelora Bung Karno',
                'negara': 'Indonesia',
                'kapasitas': '8'
            },
            {
                'id': 2,
                'nama_stadium': 'Senayan',
                'negara': 'Indonesia',
                'kapasitas': '16'
            }, 
            {
                'id': 3,
                'nama_stadium': 'Old Trafford',
                'negara': 'Inggris',
                'kapasitas': '74'
            },
            {
                'id': 4,
                'nama_stadium': 'Maracanã',
                'negara': 'Brasil',
                'kapasitas': '78'
            }
        ]
    }
    return render(request, 'daftar_stadium.html', dummy_daftar_stadium)

def daftar_event_by_stadium(request, stadium_id):
    dummy_daftar_event = {
        'stadium_id': stadium_id,
        'daftar_event': [
            {
                'id': 1,
                'nama_event': 'Badminton Open',
                'total_hadiah': 'Rp 5.000.000',
                'tanggal_mulai': '12-04-2023',
                'kategori': 'S200',
                'kapasitas_terisi': 3,
                'kapasitas_total': 8
            },
            {
                'id': 2,
                'nama_event': 'Bali Open',
                'total_hadiah': 'Rp 4.000.000',
                'tanggal_mulai': '27-04-2023',
                'kategori': 'S100',
                'kapasitas_terisi': 8,
                'kapasitas_total': 8
            },
            {
                'id': 3,
                'nama_event': 'Jakarta Invitational',
                'total_hadiah': 'Rp 7.500.000',
                'tanggal_mulai': '15-05-2023',
                'kategori': 'S300',
                'kapasitas_terisi': 4,
                'kapasitas_total': 10
            },
            {
                'id': 4,
                'nama_event': 'Surabaya Championship',
                'total_hadiah': 'Rp 3.500.000',
                'tanggal_mulai': '02-06-2023',
                'kategori': 'S150',
                'kapasitas_terisi': 6,
                'kapasitas_total': 10
            },
            {
                'id': 5,
                'nama_event': 'Yogyakarta Masters',
                'total_hadiah': 'Rp 6.000.000',
                'tanggal_mulai': '18-06-2023',
                'kategori': 'S250',
                'kapasitas_terisi': 2,
                'kapasitas_total': 6
            }
        ]
    }
    return render(request, 'daftar_event_by_stadium.html', dummy_daftar_event)

def daftar_kategori(request, stadium_id, event_id):
    daftar_stadium= [
        {
            'id': 1,
            'nama_stadium': 'Gelora Bung Karno',
            'negara': 'Indonesia',
            'kapasitas': '8'
        },
        {
            'id': 2,
            'nama_stadium': 'Senayan',
            'negara': 'Indonesia',
            'kapasitas': '16'
        }, 
        {
            'id': 3,
            'nama_stadium': 'Old Trafford',
            'negara': 'Inggris',
            'kapasitas': '74'
        },
        {
            'id': 4,
            'nama_stadium': 'Maracanã',
            'negara': 'Brasil',
            'kapasitas': '78'
        }
    ]
    daftar_event = [
        {
            'id': 1,
            'nama_event': 'Badminton Open',
            'total_hadiah': 'Rp 5.000.000',
            'tanggal_mulai': '12-04-2023',
            'tanggal_selesai': '21-04-2023',
            'kategori': 'S200',
            'kapasitas_terisi': 3,
            'kapasitas_total': 8
        },
        {
            'id': 2,
            'nama_event': 'Bali Open',
            'total_hadiah': 'Rp 4.000.000',
            'tanggal_mulai': '27-04-2023',
            'tanggal_selesai': '15-05-2023',
            'kategori': 'S100',
            'kapasitas_terisi': 8,
            'kapasitas_total': 8
        },
        {
            'id': 3,
            'nama_event': 'Jakarta Invitational',
            'total_hadiah': 'Rp 7.500.000',
            'tanggal_mulai': '15-05-2023',
            'tanggal_selesai': '28-05-2023',
            'kategori': 'S300',
            'kapasitas_terisi': 4,
            'kapasitas_total': 10
        },
        {
            'id': 4,
            'nama_event': 'Surabaya Championship',
            'total_hadiah': 'Rp 3.500.000',
            'tanggal_mulai': '02-06-2023',
            'tanggal_selesai': '21-06-2023',
            'kategori': 'S150',
            'kapasitas_terisi': 6,
            'kapasitas_total': 10
        },
        {
            'id': 5,
            'nama_event': 'Yogyakarta Masters',
            'total_hadiah': 'Rp 6.000.000',
            'tanggal_mulai': '18-06-2023',
            'tanggal_selesai': '30-06-2023',
            'kategori': 'S250',
            'kapasitas_terisi': 2,
            'kapasitas_total': 6
        }
    ]
    dummy_daftar_event = {
        'stadium': daftar_stadium[stadium_id-1],
        'event': daftar_event[event_id-1],
        'daftar_kategori': [
            {
                "kategori": "Tunggal Putra",
                "partner": "-"
            },
            {
                "kategori": "Ganda Putra",
                "partner": [
                    "Kevin Sanjaya",
                    "Marcus Gideon"
                ]
            }, 
            {
                "kategori": "Ganda Campuran",
                "partner": [
                    "Liliyana Natsir",
                    "Debby Susanto"
                ]
            }
        ]

    }
    return render(request, 'daftar_kategori.html', dummy_daftar_event)