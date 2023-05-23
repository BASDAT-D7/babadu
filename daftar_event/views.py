from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *
from datetime import date
import locale

# Create your views here.
@role_required(['ATLET'])
def daftar_stadium(request):
    # result = query_result(f"SELECT * FROM stadium WHERE")
    # print(result)
    result = query_result(f'''
        SELECT nama, alamat, kapasitas
        FROM STADIUM ;
        ''')

    list_stadium = {
            "daftar_stadium": []
        }

    for row in result:
        list_stadium["daftar_stadium"].append({
            "nama_stadium": row[0],
            "negara": row[1],
            "kapasitas": row[2]
        })
        
    return render(request, 'daftar_stadium.html', list_stadium)

@role_required(['ATLET'])
def daftar_event_by_stadium(request, nama_stadium):

    current_date = date.today()
    formatted_date = current_date.strftime("%Y-%m-%d")
    # result = query_result(f'''
    #     SELECT E.nama_event, E.total_hadiah, E.tgl_mulai, E.kategori_superseries
    #     FROM EVENT as E
    #     WHERE tgl_mulai <= '{formatted_date}' 
    #     AND E.nama_stadium = '{nama_stadium}';
    #     ''')

    result = query_result(f'''
        SELECT DISTINCT E.nama_event, E.total_hadiah, E.tgl_mulai, E.kategori_superseries, S.kapasitas, COUNT(*) as jumlah
        FROM EVENT as E
        JOIN PARTAI_PESERTA_KOMPETISI as PPK ON E.nama_event = PPK.nama_event
        JOIN STADIUM as S ON E.nama_stadium = S.nama
        WHERE tgl_mulai <= '{formatted_date}' 
        AND E.nama_stadium = '{nama_stadium}'
        GROUP BY E.nama_event, E.total_hadiah, E.tgl_mulai, E.kategori_superseries, S.kapasitas;
        ''')

    list_event_by_stadium = {
            "daftar_event": []
        }

    for row in result:
        list_event_by_stadium["daftar_event"].append({
            'nama_event': row[0],
            'total_hadiah': "Rp" + format(row[1], ","),
            'tanggal_mulai': row[2],
            'kategori': row[3],
            'kapasitas_terisi': row[5],
            'kapasitas_total': row[4]
        })

    return render(request, 'daftar_event_by_stadium.html', list_event_by_stadium)

@role_required(['ATLET'])
def daftar_kategori(request, nama_stadium, nama_event):
    result_stadium = query_result(f'''
        SELECT nama, negara
        FROM STADIUM
        WHERE nama = '{nama_stadium}';
        ''')

    result_event = query_result(f'''
        SELECT E.nama_event, E.total_hadiah, E.tgl_mulai, E.tgl_selesai, E.kategori_superseries
        FROM EVENT as E
        AND E.nama_stadium = '{nama_stadium}'
        AND E.nama_event = '{nama_event}';
        ''')

    result_kategori = query_result(f'''
        SELECT DISTINCT jenis_partai, COUNT(*) as jumlah_peserta
        FROM PARTAI_PESERTA_KOMPETISI 
        WHERE nama_event = '{nama_event}'
        GROUP BY jenis_partai, nama_event;
        ''')

    result_atlet_tanpa_pasangan = query_result(f'''
        SELECT
        ''')

    list_kategori_by_event = {
            'stadium' :[],
            'event': [],
            'daftar_kategori' : []
        }

    dummy_daftar_event = {
        'stadium': "",
        'event': "",
        'daftar_kategori': [
            {
                "kategori": "Tunggal Putra",
                "partner": "-"
            },
            {
                "kategori": "Ganda Putra",
                "partner": [
                    "Kevin Sanjaya",
                    "Marcus Gideon"
                ]
            }, 
            {
                "kategori": "Ganda Campuran",
                "partner": [
                    "Liliyana Natsir",
                    "Debby Susanto"
                ]
            }
        ]

    }
    return render(request, 'daftar_kategori.html', dummy_daftar_event)