from django.shortcuts import render
from django.http import HttpResponse
from babadu_function.authentication import *
from babadu_function.general import *

# Create your views here.
def daftar_atlet(request):
    if get_current_user(request)["user_role"] == "UMPIRE":
        daftar_atlet = {
            "kualifikasi": [],
            "non_kualifikasi": [],
            "ganda": [],
        }

        atlet_kualifikasi = query_result('''
        SELECT nama, tgl_lahir, negara_asal, play_right, height, ak.world_rank, world_tour_rank, jenis_kelamin, total_point
        FROM atlet_kualifikasi ak 
        JOIN member m ON ak.id_atlet = m.id
        JOIN atlet a ON ak.id_atlet = a.id
        JOIN (SELECT id_atlet, SUM(total_point) AS total_point FROM point_history GROUP BY id_atlet) AS t ON ak.id_atlet = t.id_atlet;
        ''')

        for row in atlet_kualifikasi:
            daftar_atlet["kualifikasi"].append({
                "nama": row[0],
                "tgl_lahir": row[1],
                "negara_asal": row[2],
                "play_right": ("Ya" if row[3] == 1 else "Tidak"),
                "height": row[4],
                "world_rank": row[5],
                "world_tour_rank": row[6],
                "jenis_kelamin": ("Laki-laki" if row[7] == 1 else "Perempuan"),
                "total_point": row[8]
            })

        atlet_non_kualifikasi = query_result('''
        SELECT nama, tgl_lahir, negara_asal, play_right, height, world_rank, jenis_kelamin
        FROM atlet_non_kualifikasi an
        JOIN member m ON an.id_atlet = m.id
        JOIN atlet a ON an.id_atlet = a.id;
        ''')

        for row in atlet_non_kualifikasi:
            daftar_atlet["non_kualifikasi"].append({
                "nama": row[0],
                "tgl_lahir": row[1],
                "negara_asal": row[2],
                "play_right": ("Ya" if row[3] == 1 else "Tidak"),
                "height": row[4],
                "world_rank": ("-" if row[5] == None else row[5]),
                "jenis_kelamin": ("Laki-laki" if row[6] == 1 else "Perempuan"),
                "total_point": 0
            })

        atlet_ganda = query_result('''
        SELECT id_atlet_ganda, m1.nama AS nama_atlet_1, m2.nama AS nama_atlet_2, t1.total_point+t2.total_point AS total_point
        FROM atlet_ganda ag
        JOIN member m1 ON ag.id_atlet_kualifikasi = m1.id
        JOIN member m2 ON ag.id_atlet_kualifikasi_2 = m2.id
        JOIN (SELECT id_atlet, SUM(total_point) AS total_point FROM point_history GROUP BY id_atlet) AS t1 ON ag.id_atlet_kualifikasi = t1.id_atlet
        JOIN (SELECT id_atlet, SUM(total_point) AS total_point FROM point_history GROUP BY id_atlet) AS t2 ON ag.id_atlet_kualifikasi_2 = t2.id_atlet;
        ''')

        for row in atlet_ganda:
            daftar_atlet["ganda"].append({
                "id_atlet_ganda": row[0],
                "nama_atlet_1": row[1],
                "nama_atlet_2": row[2],
                "total_point": row[3]
            })
        return render(request, "daftar_atlet.html", daftar_atlet)
    return HttpResponse('')