from django.shortcuts import render
from babadu_function.general import *
from datetime import datetime

def convert_date_format(date_string):
    # Membuat objek datetime dari string input dengan format yang diberikan
    date_object = datetime.strptime(date_string, "%b. %d, %Y")
    # Mengonversi objek datetime menjadi string dengan format yang diinginkan
    formatted_date = date_object.strftime("%Y-%m-%d")
    return formatted_date

# Create your views here.
def form_data_kualifikasi(request):
    if (request.method == 'POST'):
        tahun = request.POST.get('tahun')
        nomor_batch = request.POST.get('nomor_batch')
        tempat_pelaksanaan = request.POST.get('tempat_pelaksanaan')
        tanggal_pelaksanaan = request.POST.get('tanggal_pelaksanaan')

        # INSERT DATA
        query_add(f"INSERT INTO ujian_kualifikasi (tahun, batch, tempat, tanggal) VALUES ('{tahun}', '{nomor_batch}', '{tempat_pelaksanaan}', '{tanggal_pelaksanaan}');")
        
    return render(request, 'form_data_kualifikasi.html')

def list_ujian_kualifikasi(request):
    # GET DATA
    result = query_result("SELECT * FROM ujian_kualifikasi;")
    list_ujian = []  
    for i in result:
        list_ujian.append({
            "tahun": i[0],
            "batch": i[1],
            "tempat": i[2],
            "tanggal": str(i[3])
        })
    context = {
        "list_ujian": list_ujian
    }
    return render(request, 'list_ujian_kualifikasi.html', context)

def pertanyaan_kualifikasi(request, tahun, batch, tempat, tanggal):
    # SEARCH & SELECT DATA
    # TODO: HANDLE THIS
    result = query_result(f"SELECT * FROM ujian_kualifikasi WHERE tahun = '{tahun}' AND batch = '{batch}' AND tempat = '{tempat}' AND tanggal = '{tanggal}';")
    if (len(result) == 0):
        print("Data tidak ditemukan")
        return render(request, 'pertanyaan_kualifikasi.html')

    # Pertanyaan Kualifikasi
    context = {
        "pertanyaan_kualifikasi": [
            {
                "nomor": 1,
                "pertanyaan": "Apakah bulutangkis adalah olahraga raket yang dimainkan dengan menggunakan kok?",
                "jawaban": [
                    "Ya",
                    "Tidak"
                ],
                "kunci_jawaban": "Ya"
            },
            {
                "nomor": 2,
                "pertanyaan": "Apakah pemain bulutangkis diizinkan menyentuh jaring saat bermain?",
                "jawaban": [
                   "Ya",
                   "Tidak"
                ],
                "kunci_jawaban": "Tidak"
            },
            {
                "nomor": 3,
                "pertanyaan": "Apakah setiap pemain bulutangkis diperbolehkan memegang raket dengan kedua tangan?",
                "jawaban": [
                    "Ya",
                    "Tidak"
                ],
                "kunci_jawaban": "Ya"

            },
            {
                "nomor": 4,
                "pertanyaan": "Apakah permainan bulutangkis dimainkan oleh dua orang atau lebih?",
                "jawaban": [
                    "Ya",
                    "Tidak"
                ],
                "kunci_jawaban": "Ya"
            },
            {
                "nomor": 5,
                "pertanyaan": "Apakah poin tertinggi dalam permainan bulutangkis adalah 21 poin?",
                "jawaban": [
                    "Ya",
                    "Tidak"
                ],
                "kunci_jawaban": "Ya"
            }
        ],
        "tahun": tahun,
        "batch": batch,
        "tempat": tempat,
        "tanggal": str(tanggal)
    }

    # Jawaban Soal
    if (request.method == 'POST'):
        jawaban_soal_1 = request.POST.get('jawaban_soal_1')
        jawaban_soal_2 = request.POST.get('jawaban_soal_2')
        jawaban_soal_3 = request.POST.get('jawaban_soal_3')
        jawaban_soal_4 = request.POST.get('jawaban_soal_4')
        jawaban_soal_5 = request.POST.get('jawaban_soal_5')
        
        # Koreksi
        jawaban_benar = 0
        jawaban_benar += 1 if (jawaban_soal_1 == context['pertanyaan_kualifikasi'][0]['kunci_jawaban']) else 0
        jawaban_benar += 1 if (jawaban_soal_2 == context['pertanyaan_kualifikasi'][1]['kunci_jawaban']) else 0
        jawaban_benar += 1 if (jawaban_soal_3 == context['pertanyaan_kualifikasi'][2]['kunci_jawaban']) else 0
        jawaban_benar += 1 if (jawaban_soal_4 == context['pertanyaan_kualifikasi'][3]['kunci_jawaban']) else 0
        jawaban_benar += 1 if (jawaban_soal_5 == context['pertanyaan_kualifikasi'][4]['kunci_jawaban']) else 0

        # INSERT DATA
        user_id = request.COOKIES.get('user_id')
        hasil_lulus = True if (jawaban_benar >= 4) else False
        query_add(f"""
                    INSERT INTO atlet_nonkualifikasi_ujian_kualifikasi (id_atlet, tahun, batch, tempat, tanggal, hasil_lulus)
                    VALUES ('{user_id}',
                        '{tahun}',
                        '{batch}',
                        '{tempat}',
                        '{tanggal}',
                        '{hasil_lulus}');
                    """)
        print(hasil_lulus)

    return render(request, 'pertanyaan_kualifikasi.html', context)

def riwayat_ujian_kualifikasi(request):
    # GET DATA
    result = query_result("SELECT * FROM atlet_nonkualifikasi_ujian_kualifikasi;")
    riwayat_ujian = []  
    for i in result:
        riwayat_ujian.append({
            "nama_atlet": parse(query_result(f"SELECT nama FROM member WHERE id = '{i[0]}';")),
            "tahun": i[1],
            "batch": i[2],
            "tempat": i[3],
            "tanggal": str(i[4]),
            "hasil": "Lulus" if i[5] else "Tidak Lulus"
        })
    context = {
        "riwayat_ujian": riwayat_ujian
    }
    return render(request, 'riwayat_ujian_kualifikasi.html', context)