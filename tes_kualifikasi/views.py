from django.shortcuts import render

# Create your views here.
def form_data_kualifikasi(request):
    dummy_form_settings = {
        "tempat_pelaksanaan": [
            "Gor Bulutangkis Jakarta",
            "Gor Bulutangkis Surabaya",
            "Gor Bulutangkis Bandung"
        ],
        "tanggal_pelaksanaan": [
            "06/05/2023",
            "07/05/2023",
            "08/05/2023",
            "09/05/2023",
            "10/05/2023"
        ]

    }
    return render(request, 'form_data_kualifikasi.html', dummy_form_settings)

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
