from django.shortcuts import render

# Create your views here.
def daftar_stadium(request):
    dummy_daftar_event = {
        'daftar_event': [
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
    return render(request, 'daftar_stadium.html', dummy_daftar_event)

def daftar_event_by_stadium(request, id):
    dummy_daftar_event = {
        'daftar_event': [
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
    return render(request, 'daftar_event_by_stadium.html', dummy_daftar_event)

def daftar_kategori(request, id):
    dummy_daftar_event = {
        'daftar_event': [
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
    return render(request, 'daftar_kategori.html', dummy_daftar_event)