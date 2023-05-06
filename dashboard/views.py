from django.shortcuts import render

# Create your views here.
def dashboard_atlet(request):
    dummy_atlet = {
        "nama_lengkap": "Eugenius Mario Situmorang",
        "negara": "Indonesia",
        "email": "eugeniusms@gmail.com",
        "tanggal_lahir": "13 Mei 2002",
        "play": "Right",
        "tinggi_badan": "175cm",
        "jenis_kelamin": "Laki",
        "pelatih": "Richard Feynman",
        "status": "Qualified",
        "world_rank": "#1182",
        "total_poin": "82150",
    }
    return render(request, 'dashboard_atlet.html', dummy_atlet)

def dashboard_pelatih(request):
    dummy_pelatih = {
        "nama_lengkap": "Richard Feynman",
        "negara": "Indonesia",
        "email": "richardfeynman@gmail.com",
        "spesialisasi_kategori": [
            "Tunggal Putra",
            "Ganda Putra",
            "Ganda Campuran",
        ],
        "tanggal_mulai": "6 Mei 2023",
    }
    return render(request, 'dashboard_pelatih.html', dummy_pelatih)

def dashboard_umpire(request):
    return render(request, 'dashboard_umpire.html')