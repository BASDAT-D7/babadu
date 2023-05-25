from django.shortcuts import render
from django.http import HttpResponse
from babadu_function.authentication import *
from babadu_function.general import *

# Create your views here.
@role_required(['UMPIRE'])
def hasil_pertandingan(request, pertandingan):
    if get_current_user(request)["user_role"] == "UMPIRE":
        [ partai, nama, tahun ] = pertandingan.split("-")
        hasil_pertandingan = {
            'partai_kompetisi': dict(),
            'daftar_tahap': []
        }
        
        # Get detail dari partai kompetisi
        result = query_result(f'''
        SELECT pk.nama_event, pk.jenis_partai, nama_stadium, total_hadiah, kategori_superseries, tgl_mulai, tgl_selesai, k.kapasitas, s.kapasitas
        FROM partai_kompetisi pk
        JOIN event e on pk.nama_event = e.nama_event
        JOIN stadium s on e.nama_stadium = s.nama
        JOIN (SELECT nama_event, jenis_partai, COUNT(nomor_peserta) AS kapasitas FROM partai_peserta_kompetisi GROUP BY nama_event, jenis_partai) AS k 
            ON pk.nama_event = k.nama_event AND pk.jenis_partai = k.jenis_partai
        WHERE pk.jenis_partai = '{partai}' AND pk.nama_event = '{nama}' AND tahun_event = '{tahun}';
        ''')

        for row in result:
            hadiah = 'Rp {:,.2f}'.format(row[3]).replace(",", "#").replace(".", ",").replace("#",".")
            hasil_pertandingan["partai_kompetisi"].update({
                "nama_event": row[0],
                "jenis_partai": row[1],
                "stadium": row[2],
                "hadiah": hadiah,
                "kategori": row[4],
                "tgl_mulai": row[5],
                "tgl_selesai": row[6],
                "kapasitas": row[7],
                "max_kapasitas": row[8]
            })

        # Get detail dari hasil pertandingan
        result = query_result(f'''
            SELECT jenis_babak, STRING_AGG(CONCAT(ag.nama_ganda, nama), ', ') AS nama
            FROM (
                SELECT jenis_babak, id_atlet_ganda, id_atlet_kualifikasi
                FROM (
                    SELECT nomor_peserta 
                    FROM partai_peserta_kompetisi 
                    WHERE jenis_partai = '{partai}' AND nama_event = '{nama}' AND tahun_event = '{tahun}') ppk
                NATURAL JOIN peserta_kompetisi pk
                NATURAL JOIN peserta_mengikuti_match pmm
                WHERE status_menang = 't') p
            LEFT OUTER JOIN (
                SELECT id_atlet_ganda, CONCAT(m1.nama, ' & ', m2.nama) AS nama_ganda
                FROM atlet_ganda ag
                JOIN member m1 ON ag.id_atlet_kualifikasi = m1.id
                JOIN member m2 ON ag.id_atlet_kualifikasi_2 = m2.id) ag ON p.id_atlet_ganda = ag.id_atlet_ganda
            LEFT OUTER JOIN member m ON p.id_atlet_kualifikasi = m.id
            GROUP BY jenis_babak;
        ''')

        if len(result) == 0:
            return render(request, 'hasil_pertandingan.html', hasil_pertandingan)

        tahap_order = ["Juara 1", "Juara 2", "Juara 3", "Semifinal", "Perempat Final", "R16", "R32"]

        for row in result:
            daftar_tim = row[1].split(", ")
            hasil_pertandingan["daftar_tahap"].append({
                "jenis_babak": row[0],
                "daftar_tim": daftar_tim
            })

        hasil_pertandingan["daftar_tahap"] = sorted(hasil_pertandingan["daftar_tahap"], key=lambda x:tahap_order.index(x["jenis_babak"]))
        return render(request, 'hasil_pertandingan.html', hasil_pertandingan)
    return HttpResponse('')