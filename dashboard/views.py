from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *

# Create your views here.
def dashboard(request):
    if is_authenticated(request) == False:
        return HttpResponseRedirect(reverse('authentication:authentication'))

    # IF ROLE ATLET LOGGED IN
    if request.COOKIES.get('user_role') == "ATLET":
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
        pelatih = parse(query_result(f"""
                                        SELECT nama
                                        FROM member
                                        JOIN atlet_pelatih ON member.id_pelatih = atlet_pelatih.id_pelatih
                                        WHERE atlet_pelatih.id_atlet = '{user_id}';
                                        """
                                    ))
        # SET CONTEXT
        dummy_atlet = {
            "nama_lengkap": nama_lengkap,
            "negara": negara,
            "email": email,
            "tanggal_lahir": tanggal_lahir,
            "play": play,
            "tinggi_badan": f"{tinggi_badan}cm",
            "jenis_kelamin": jenis_kelamin,
            "pelatih": pelatih,
            "status": "Qualified",
            "world_rank": world_rank,
            "total_poin": "82150",
        }
        return render(request, 'dashboard_atlet.html', dummy_atlet)
    
    # IF ROLE PELATIH LOGGED IN
    if request.COOKIES.get('user_role') == "PELATIH":
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

    # IF ROLE UMPIRE LOGGED IN
    if request.COOKIES.get('user_role') == "UMPIRE":
         # QUERY DATABASE
        user_id = request.COOKIES.get('user_id')
        nama_lengkap = parse(query_result(f"SELECT nama FROM member WHERE id='{user_id}';"))
        negara = parse(query_result(f"SELECT negara FROM umpire WHERE id='{user_id}';"))
        email = parse(query_result(f"SELECT email FROM member WHERE id='{user_id}';"))
        # SET CONTEXT
        dummy_umpire = {
            "nama_lengkap": nama_lengkap,
            "negara": negara,
            "email": email
        }
        return render(request, 'dashboard_umpire.html', dummy_umpire)