from django.shortcuts import render
from django.http import HttpResponse
from babadu_function.authentication import *
from babadu_function.general import *
import locale

# Create your views here.
@role_required(['UMPIRE'])
def hasil_pertandingan(request, pertandingan):
    if get_current_user(request)["user_role"] == "UMPIRE":
        locale.setlocale(locale.LC_ALL, 'id-ID')
        [ partai, nama, tahun ] = pertandingan.split("-")
        
        result = query_result(f'''
        SELECT pk.nama_event, jenis_partai, nama_stadium, total_hadiah, kategori_superseries, tgl_mulai, tgl_selesai, k.kapasitas, s.kapasitas
        FROM partai_kompetisi pk
        JOIN event e on pk.nama_event = e.nama_event
        JOIN stadium s on e.nama_stadium = s.nama
        JOIN (SELECT nama_event, COUNT(nomor_peserta) AS kapasitas FROM partai_peserta_kompetisi GROUP BY nama_event) AS k ON pk.nama_event = k.nama_event
        WHERE jenis_partai = '{partai}' AND pk.nama_event = '{nama}' AND tahun_event = '{tahun}';
        ''')

        hasil_pertandingan = {
            'partai_kompetisi': dict(),
            'daftar_tahap': [
                {
                    "nama_tahap": "Juara 1",
                    "daftar_tim": [
                        "A"
                    ]
                },
                {
                    "nama_tahap": "Juara 2",
                    "daftar_tim": [
                        "G"
                    ]
                },
                {
                    "nama_tahap": "Juara 3",
                    "daftar_tim": [
                        "D"
                    ]
                },
                {
                    "nama_tahap": "Semifinal",
                    "daftar_tim": [
                        "E"
                    ]
                },
                {
                    "nama_tahap": "Perempat Final",
                    "daftar_tim": [
                        "C", "F", "B", "H"
                    ]
                }
            ]
        }

        for row in result:
            hasil_pertandingan["partai_kompetisi"].update({
                "nama_event": row[0],
                "jenis_partai": row[1],
                "stadium": row[2],
                "hadiah": locale.currency(row[3], grouping=True),
                "kategori": row[4],
                "tgl_mulai": row[5],
                "tgl_selesai": row[6],
                "kapasitas": row[7],
                "max_kapasitas": row[8]
            })

        # TODO: TAHAP
        return render(request, 'hasil_pertandingan.html', hasil_pertandingan)
    return HttpResponse('')