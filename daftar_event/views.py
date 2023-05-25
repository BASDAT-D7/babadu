from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *
from datetime import date
import uuid

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
        JOIN ATLET as A ON PK.id_atlet_kualifikasi= A.id
        JOIN MEMBER as M ON A.id = M.id
        WHERE PPK.nama_event = '{nama_event}'
        AND PPK.jenis_partai LIKE 'G%'
        AND PK.id_atlet_ganda NOT IN (
            SELECT PK2.id_atlet_ganda
            FROM PESERTA_KOMPETISI as PK2
            GROUP BY PK2.id_atlet_ganda
            HAVING COUNT(*) = 2
        )
        GROUP BY PPK.jenis_partai, PPK.nama_event;
        ''')

    list_kategori_by_event = {
            'stadium_event' :[],
            'daftar_kategori' : [],
            'daftar_pemain' : [],
            'jenis_kelamin' : jenis_kelamin
        }

    partai_dict = {
        "TA": "Tunggal Putra",
        "TI": "Tunggal Putri",
        "GA": "Ganda Putra",
        "GI" : "Ganda Putri",
        "GC" : "Ganda Campuran"

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
            'kategori': partai_dict[row[0]],
            'jumlah_peserta' : row[1]
        })

    for row in result_pemain_tunggal:
        pasangan = row[0].split(',')
        list_kategori_by_event["daftar_pemain"].append({
            'pasangan': pasangan,
            'partai' : partai_dict[row[1]]
        })

    print(user_id)


    return render(request, 'daftar_kategori.html', list_kategori_by_event)

@role_required(['ATLET'])
def tambah_peserta(request, nama_stadium, nama_event, nama_kategori):
    if request.method == 'POST':
        selected_partner = request.POST.get('partner')
        new_atletganda_uuid = uuid.uuid4()
        user_id = request.COOKIES.get('user_id')

        if(nama_kategori.__contains__("Ganda")):
            if(selected_partner!="-"):
                result_pemain_tunggal = query_result(f'''
                SELECT PK.id_atlet_ganda, PK.id_atlet_kualifikasi
                FROM MEMBER as M
                JOIN ATLET as A ON A.id = M.id
                JOIN PESERTA_KOMPETISI as PK ON PK.id_atlet_kualifikasi = M.id
                WHERE M.nama = '{selected_partner}';
                ''')
            
                uuid_atlet_ganda_pasangan = result_pemain_tunggal[0][0]
                uuid_atlet_kualifikasi_pasangan = result_pemain_tunggal[0][1]

                
                
                result_pemain_tunggal = query_result(f'''
                SELECT *
                FROM ATLET_GANDA
                WHERE 
                ((id_atlet_kualifikasi = '{uuid_atlet_kualifikasi_pasangan}' AND id_atlet_kualifikasi_2 = '{user_id}') OR (id_atlet_kualifikasi = '{user_id}' AND id_atlet_kualifikasi_2 = '{uuid_atlet_kualifikasi_pasangan}'));
                ''')

                if(len(result_pemain_tunggal)==0):
                    query_add(f'''
                    INSERT INTO ATLET_GANDA VALUES ('{new_atletganda_uuid}', '{uuid_atlet_kualifikasi_pasangan}', '{user_id}')
                    ''')
        
        result_jumlah_peserta_kompetisi = query_result(f'''
        SELECT COUNT(*)
        FROM PESERTA_KOMPETISI;
        ''')

        id_peserta_kompetisi = result_jumlah_peserta_kompetisi[0][0]+1

        result_PESERTA = query_result(f'''
            SELECT world_rank, world_tour_rank
            FROM ATLET_KUALIFIKASI
            WHERE id_atlet = '{user_id}';
            ''')

        world_rank = result_PESERTA[0][0]
        world_rank_tour = result_PESERTA[0][1]

        if(nama_kategori.__contains__("Ganda")):
            query_add(f'''
                INSERT INTO PESERTA_KOMPETISI (nomor_peserta, id_atlet_ganda, world_rank, world_tour_rank) VALUES ('{id_peserta_kompetisi}', '{new_atletganda_uuid}', '{world_rank}', '{world_rank_tour}')
                ''')
        else:
            query_add(f'''
                INSERT INTO PESERTA_KOMPETISI (nomor_peserta, id_atlet_ganda, id_atlet_kualifikasi, world_rank, world_tour_rank) VALUES ('{id_peserta_kompetisi}', '{new_atletganda_uuid}', '{user_id}', '{world_rank}', '{world_rank_tour}')
                ''')
        
        partai_dict = {
            "Tunggal Putra": "TA",
            "Tunggal Putri": "TI",
            "Ganda Putra": "GA",
            "Ganda Putri" : "GI",
            "Ganda Campuran" : "GC"
        }

        jenis_partai = partai_dict[nama_kategori]

        result_tahun_event = query_result(f'''
            SELECT tahun
            FROM EVENT
            WHERE nama_event = '{nama_event}'
            AND nama_stadium = '{nama_stadium}';
            ''')

        tahun_event = result_tahun_event[0][0]

        query_add(f'''
                INSERT INTO PARTAI_PESERTA_KOMPETISI VALUES ('{jenis_partai}', '{nama_event}', '{tahun_event}', '{id_peserta_kompetisi}')
                ''')

        

    return daftar_kategori(request, nama_stadium=nama_stadium, nama_event=nama_event)
    