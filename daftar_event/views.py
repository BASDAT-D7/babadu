from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *
from datetime import date

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
            'kapasitas_total': row[4],
            'nama_stadium' : nama_stadium
        })

    return render(request, 'daftar_event_by_stadium.html', list_event_by_stadium)

@role_required(['ATLET'])
def daftar_kategori(request, nama_stadium, nama_event):

    user_id = request.COOKIES.get('user_id')

    result_current_user = query_result(f'''
        SELECT jenis_kelamin
        FROM ATLET
        WHERE id = '{user_id}';
        ''')
    
    jenis_kelamin = result_current_user[0][0]

    result_stadium_event = query_result(f'''
        SELECT DISTINCT E.nama_event, E.total_hadiah, E.tgl_mulai, E.tgl_selesai, E.kategori_superseries, COUNT(*) as jumlah, S.kapasitas, S.nama, S.negara
        FROM EVENT as E
        JOIN PARTAI_PESERTA_KOMPETISI as PPK ON E.nama_event = PPK.nama_event
        JOIN STADIUM as S ON E.nama_stadium = S.nama
        AND E.nama_stadium = '{nama_stadium}'
        GROUP BY E.nama_event, E.total_hadiah, E.tgl_mulai, E.kategori_superseries, S.kapasitas, E.tgl_selesai, E.kategori_superseries, S.nama, S.negara;
        ''')

    result_kategori = query_result(f'''
        SELECT DISTINCT jenis_partai, COUNT(*) as jumlah_peserta
        FROM PARTAI_PESERTA_KOMPETISI 
        WHERE nama_event = '{nama_event}'
        GROUP BY jenis_partai, nama_event;
        ''')

    result_pemain_tunggal = query_result(f'''
        SELECT DISTINCT COALESCE(STRING_AGG(M.nama, ', '), '-') as nama_pasangan, PPK.jenis_partai, PPK.nama_event 
        FROM PARTAI_PESERTA_KOMPETISI as PPK
        JOIN PESERTA_KOMPETISI as PK ON PK.nomor_peserta = PPK.nomor_peserta
        JOIN ATLET_GANDA as AG ON AG.id_atlet_ganda = PK.id_atlet_ganda
        JOIN ATLET as A ON AG.id_atlet_kualifikasi= A.id
        JOIN MEMBER as M ON A.id = M.id
        WHERE PPK.nama_event = '{nama_event}'
        AND A.jenis_kelamin = '{jenis_kelamin}'
        AND PK.id_atlet_ganda IN (
            SELECT PK2.id_atlet_ganda
            FROM PESERTA_KOMPETISI as PK2
            GROUP BY PK2.id_atlet_ganda
            HAVING COUNT(*) = 1
        )
        GROUP BY PPK.jenis_partai, PPK.nama_event;
        ''')

    list_kategori_by_event = {
            'stadium_event' :[],
            'daftar_kategori' : [],
            'daftar_pemain' : [],
            'jenis_kelamin' : jenis_kelamin
        }


    for row in result_stadium_event:
        list_kategori_by_event["stadium_event"].append({
            'nama_event': row[0],
            'total_hadiah': "Rp" + format(row[1], ","),
            'tanggal_mulai': row[2],
            'tanggal_selesai': row[3],
            'kategori': row[4],
            'kapasitas_terisi': row[5],
            'kapasitas_total': row[6],
            'nama_stadium' : row[7],
            'negara' : row[8]
        })
    
    
    for row in result_kategori:
        list_kategori_by_event["daftar_kategori"].append({
            'kategori': row[0],
            'jumlah_peserta' : row[1]
        })

    for row in result_pemain_tunggal:
        pasangan = row[0].split(',')
        list_kategori_by_event["daftar_pemain"].append({
            'pasangan': pasangan,
            'partai' : row[1]
        })


    return render(request, 'daftar_kategori.html', list_kategori_by_event)