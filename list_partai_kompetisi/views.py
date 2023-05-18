from django.shortcuts import render
from django.http import HttpResponse
from babadu_function.authentication import *
from babadu_function.general import *

# Create your views here.
def list_partai_kompetisi(request):
    if get_current_user(request)["user_role"] == "UMPIRE":
        result = query_result('''
        SELECT pk.nama_event, tahun_event, nama_stadium, jenis_partai, kategori_superseries, tgl_mulai, tgl_selesai, k.kapasitas, s.kapasitas
        FROM partai_kompetisi pk
        JOIN event e on pk.nama_event = e.nama_event
        JOIN stadium s on e.nama_stadium = s.nama
        JOIN (SELECT nama_event, COUNT(nomor_peserta) AS kapasitas FROM partai_peserta_kompetisi GROUP BY nama_event) AS k ON pk.nama_event = k.nama_event;
        ''')

        partai_kompetisi = {
            'partai_kompetisi': []
        }

        for row in result:
            partai_kompetisi["partai_kompetisi"].append({
                "nama_event": row[0],
                "tahun": row[1],
                "stadium": row[2],
                "jenis_partai": row[3],
                "kategori": row[4],
                "tgl_mulai": row[5],
                "tgl_selesai": row[6],
                "kapasitas": row[7],
                "max_kapasitas": row[8]
            })
        return render(request, 'partai_kompetisi.html', partai_kompetisi)
    return HttpResponse('')