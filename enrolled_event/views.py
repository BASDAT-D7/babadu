from django.http import HttpResponseRedirect
from django.urls import reverse
from babadu_function.general import *
from django.shortcuts import render
from babadu_function.authentication import *

# Create your views here.

@role_required(['ATLET'])
def enrolled_event(request):
    # GET DATA
    user_id = get_current_user(request)["user_id"]
    result = query_result(f"""SELECT E.nama_event, E.tahun, E.nama_stadium, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai
            FROM ATLET A JOIN ATLET_KUALIFIKASI AK ON id = id_atlet
            JOIN PESERTA_KOMPETISI PK ON id_atlet = id_atlet_kualifikasi
            JOIN PESERTA_MENDAFTAR_EVENT PME ON PK.nomor_peserta = PME.nomor_peserta
            JOIN EVENT E ON PME.nama_event = E.nama_event AND PME.tahun = E.tahun
            WHERE A.id = '{user_id}' ;""")
    list_enrolled_event = []  
    for row in result:
        list_enrolled_event.append({
            "nama_event": row[0],
            "tahun": row[1],
            "stadium": row[2],
            "kategori": row[3],
            "tgl_mulai": row[4],
            "tgl_selesai": row[5]    
        })
    context = {
        "list_enrolled_event": list_enrolled_event,
        "role": get_current_user(request)["user_role"]
    }
    return render(request, 'enrolled_event.html', context)

@role_required(['ATLET'])
def unenrolled_event(request): #delete
    # GET DATA
    user_id = get_current_user(request)["user_id"]
    result = query_result(f"""SELECT E.nama_event, E.tahun, E.nama_stadium, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai
        FROM ATLET A JOIN ATLET_KUALIFIKASI AK ON id = id_atlet
        JOIN PESERTA_KOMPETISI PK ON id_atlet = id_atlet_kualifikasi
        JOIN PESERTA_MENDAFTAR_EVENT PME ON PK.nomor_peserta = PME.nomor_peserta
        JOIN EVENT E ON PME.nama_event = E.nama_event AND PME.tahun = E.tahun
        WHERE A.id = '{user_id}' ;""")
    list_result = []  
    for row in result:
        list_result.append({
            "nama_event": row[0],
            "tahun": row[1],
            "stadium": row[2],
            "kategori": row[3],
            "tgl_mulai": row[4],
            "tgl_selesai": row[5]    
        })

    query_result(f"""DELETE FROM PESERTA_MENDAFTAR_EVENT pme 
                WHERE pme.nama_event = '{"nama_event"}' AND pme.tahun = '{"tahun"}' AND pme.nomor_peserta IN (
                    SELECT pk.nomor_peserta 
                    FROM PESERTA_KOMPETISI pk 
                    LEFT JOIN ATLET_GANDA ag ON ag.id_atlet_ganda = pk.id_atlet_ganda 
                    WHERE ag.id_atlet_kualifikasi = '{user_id}' or ag.id_atlet_kualifikasi_2 = '{user_id}' or pk.id_atlet_kualifikasi = '');""")

    response = HttpResponseRedirect(reverse("enrolled_event:enrolled_event"))
  
        
    context = {
        "send_data_is_valid": True
    }
    return render(request, 'enrolled_event.html',  context)

@role_required(['ATLET'])
def enrolled_partai(request):
    # GET DATA
    user_id = get_current_user(request)["user_id"]
    result = query_result(f"""SELECT E.nama_event, E.tahun, E.nama_stadium, PI.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai
            FROM ATLET A JOIN ATLET_KUALIFIKASI AK ON id = id_atlet
            JOIN PESERTA_KOMPETISI PK ON id_atlet = id_atlet_kualifikasi
            JOIN PESERTA_MENDAFTAR_EVENT PME ON PK.nomor_peserta = PME.nomor_peserta
            JOIN EVENT E ON PME.nama_event = E.nama_event AND PME.tahun = E.tahun
            JOIN PARTAI_KOMPETISI PI ON PME.nama_event = PI.nama_event AND PME.tahun = PI.tahun_event
            WHERE A.id = '{user_id}' ;""")
    list_enrolled_partai = []  
    for row in result:
        list_enrolled_partai.append({
            "nama_event": row[0],
            "tahun": row[1],
            "stadium": row[2],
            "jenis_partai": row[3],
            "kategori": row[4],
            "tgl_mulai": row[5],
            "tgl_selesai": row[6]    
        })
    context = {
        "list_enrolled_partai": list_enrolled_partai,
        "role": get_current_user(request)["user_role"]
    }
    return render(request, 'enrolled_partai.html', context)

