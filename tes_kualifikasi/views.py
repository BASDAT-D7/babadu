from django.shortcuts import render
from babadu_function.general import *

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
    result = query_result("SELECT * FROM ujian_kualifikasi;")
    list_ujian = []  
    for i in result:
        list_ujian.append({
            "tahun": i[0],
            "batch": i[1],
            "tempat": i[2],
            "tanggal": i[3]
        })
    context = {
        "list_ujian": list_ujian
    }
    print(context)
    return render(request, 'list_ujian_kualifikasi.html', context)

def pertanyaan_kualifikasi(request):
    dummy_pertanyaan = {
        "pertanyaan_kualifikasi": [
            {
                "nomor": 1,
                "pertanyaan": "Apakah anda pernah mengikuti kejuaraan bulutangkis sebelumnya?",
                "jawaban": [
                    "Ya",
                    "Tidak"
                ]
            },
            {
                "nomor": 2,
                "pertanyaan": "Bagaimana hasil kejuaraan bulutangkis sebelumnya?",
                "jawaban": [
                    "Juara",
                    "Runner Up",
                    "Semi Final",
                    "Perempat Final",
                    "Tidak Sama Sekali"
                ]
            },
            {
                "nomor": 3,
                "pertanyaan": "Mengapa anda ingin mengikuti kejuaraan bulutangkis ini?",
                "jawaban": [
                    "Untuk mengasah kemampuan",
                    "Untuk mengisi waktu luang",
                    "Untuk mengikuti jejak orang tua",
                    "Alasan lainnya"
                ]
            },
            {
                "nomor": 4,
                "pertanyaan": "Berapa lama anda bermain bulutangkis?",
                "jawaban": [
                    "Kurang dari 1 tahun",
                    "1 - 2 tahun",
                    "2 - 3 tahun",
                    "Lebih dari 3 tahun"
                ]
            }
        ]
    }
    return render(request, 'pertanyaan_kualifikasi.html', dummy_pertanyaan)
