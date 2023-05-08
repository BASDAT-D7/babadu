from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *

# Create your views here.
def dashboard_atlet(request):
    if is_authenticated(request) == False:
        return HttpResponseRedirect(reverse('authentication:authentication'))
    
    # QUERY DATABASE
    user_id = request.COOKIES.get('user_id')
    nama_lengkap = parse(query_result(f"SELECT nama FROM member WHERE id='{user_id}';"))
    negara = parse(query_result(f"SELECT negara_asal FROM atlet WHERE id='{user_id}';"))
    email = parse(query_result(f"SELECT email FROM member WHERE id='{user_id}';"))
    tanggal_lahir = parse(query_result(f"SELECT tgl_lahir FROM atlet WHERE id='{user_id}';"))
    play = "Right" if parse(query_result(f"SELECT play_right FROM atlet WHERE id='{user_id}';")) else "Left"
    tinggi_badan = parse(query_result(f"SELECT height FROM atlet WHERE id='{user_id}';"))
    jenis_kelamin = "Laki" if parse(query_result(f"SELECT jenis_kelamin FROM atlet WHERE id='{user_id}';")) else "Perempuan"
    world_rank = "-" if parse(query_result(f"SELECT world_rank FROM atlet WHERE id='{user_id}';")) == None else "#"+parse(query_result(f"SELECT world_rank FROM atlet WHERE id='{user_id}';"))

    # SET CONTEXT
    dummy_atlet = {
        "nama_lengkap": nama_lengkap,
        "negara": negara,
        "email": email,
        "tanggal_lahir": tanggal_lahir,
        "play": play,
        "tinggi_badan": f"{tinggi_badan}cm",
        "jenis_kelamin": jenis_kelamin,
        "pelatih": "Richard Feynman",
        "status": "Qualified",
        "world_rank": world_rank,
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
    dummy_umpire = {
        "nama_lengkap": "Dek Depe",
        "negara": "Indonesia",
        "email": "dekdepe@gmail.com"
    }
    return render(request, 'dashboard_umpire.html', dummy_umpire)