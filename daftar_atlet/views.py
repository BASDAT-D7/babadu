from django.shortcuts import render

# Create your views here.
def daftar_atlet(request):
    dummy_daftar_atlet = {
        "daftar_atlet": [
            {
                "nama_lengkap": "Eugenius Mario Situmorang",
            },
            {
                "nama_lengkap": "Peokra Mokra",
            },
            {
                "nama_lengkap": "Aegon Targaryen",
            },
        ]  
    }
    return render(request, 'daftar_atlet.html', dummy_daftar_atlet)