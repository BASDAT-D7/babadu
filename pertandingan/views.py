from django.shortcuts import render
from babadu_function.authentication import *
from babadu_function.general import *
from django.http import *

# Create your views here.
@role_required(['UMPIRE'])
def perempat_final(request):
    dummy_perempat_final = {
        'daftar_perempat_final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'B',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
            {
                'id': 2,
                'tim_1': 'C',
                'tim_2': 'D',
                'skor_tim_1': 1,
                'skor_tim_2': 2
            },
            {
                'id': 3,
                'tim_1': 'E',
                'tim_2': 'F',
                'skor_tim_1': 2,
                'skor_tim_2': 1
            },
            {
                'id': 4,
                'tim_1': 'G',
                'tim_2': 'H',
                'skor_tim_1': 2,
                'skor_tim_2': 1
            }
        ]
    }           
    return render(request, 'pertandingan_perempat_final.html', dummy_perempat_final)

@role_required(['UMPIRE'])
def semifinal(request):
    dummy_semifinal = {
        'daftar_perempat_final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'D',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
            {
                'id': 2,
                'tim_1': 'E',
                'tim_2': 'G',
                'skor_tim_1': 1,
                'skor_tim_2': 2
            },
        ]
    }
    return render(request, 'pertandingan_semifinal.html', dummy_semifinal)

@role_required(['UMPIRE'])
def final(request):
    dummy_final = {
        'perebutan_juara_tiga': [
            {
                'id': 2,
                'tim_1': 'D',
                'tim_2': 'E',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
        ],
        'final': [
            {
                'id': 1,
                'tim_1': 'A',
                'tim_2': 'G',
                'skor_tim_1': 1,
                'skor_tim_2': 0
            },
        ]
    }

    #
    # # alter table peserta_mengikuti match to add new attributes
    # query_add('''
    #     CREATE TABLE hasil_pertandingan
    #     ADD nama_tim1 VARCHAR(100),
    #     ADD nama_tim2 VARCHAR(100),
    #     ADD skor_tim1 INT,
    #     ADD skor_tim2 INT;
    # ''')

    list_match = {
        "perebutan_juara_tiga": [],
        "final": []
    }

    # Pertandingan Juara 3
    pertandingan_juara_tiga = []

    random_team1 = query_result('''
        SELECT *
        FROM partai_peserta_kompetisi ppk
        ORDER BY RANDOM()
        LIMIT 2;
    ''')
    random_team2 = query_result('''
        SELECT m.nama
        FROM partai_peserta_kompetisi ppk
        JOIN peserta_kompetisi pk ON ppk.nomor_peserta = pk.nomor_peserta
        JOIN atlet_kualifikasi ak ON pk.id_atlet_kulaifikasi = ak.id_atlet
        JOIN atlet a ON ak.id_atlet = a.id
        JOIN member m ON a.id = m.id
        ORDER BY RANDOM()
        LIMIT 2;
    ''')
    random_match = [random_team1, random_team2]

    pertandingan_juara_tiga.append(random_match)

    # for i in range(len(pertandingan_juara_tiga)):
    #     list_match["perebutan_juara_tiga"].append({
    #         "id": i,
    #         "tim_1": pertandingan_juara_tiga[i][0],
    #         "tim_2": pertandingan_juara_tiga[i][1],
    #         "skor_tim_1": ("Ya" if row[3] == 1 else "Tidak"),
    #         "skor_tim_2": row[4]
    #     })
    #
    # if request.method == "POST":
    #     match_juara_tiga = list_match_final.get("perebutan_juara_tiga")
    #     match_final = list_match_final.get("final")
    #         if item.
    #
    #     user_id = get_current_user(request)["user_id"]
    #     id_atlet = request.POST.get('atlet')
    #     query_add(f'''
    #         INSERT INTO match VALUES
    #         ('{user_id}', '{id_atlet}'),
    #         ;
    #     ''')
    #
    #     return render(request, 'pertandingan_final_dan_juara_tiga.html', dummy_final)
    # else:
    #     return HttpResponse("ERROR")

    return render(request, 'pertandingan_final_dan_juara_tiga.html', dummy_final)

# def add_transport(request):
#     if request.method == "POST":
#         form = TransportationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             request.session['last_activity'] = "add transportation"
#             return HttpResponse("Transportasi: " + form.cleaned_data['name'] + " berhasil ditambahkan!")
#         else:
#             return HttpResponse("Transportasi tidak berhasil ditambahkan!")
#
#     context = {'form': TransportationForm()}
#     return render(request, 'add_transportation.html', context)