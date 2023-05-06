from django.shortcuts import render

# Create your views here.
def daftar_event(request):
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
    return render(request, 'daftar_event.html', dummy_daftar_event)