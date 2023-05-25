from django.http import HttpResponseRedirect
from django.urls import reverse
from babadu_function.general import *
from django.shortcuts import render
from babadu_function.authentication import *
from datetime import datetime

def convert_date_format(date_string):
    # Membuat objek datetime dari string input dengan format yang diberikan
    date_object = datetime.strptime(date_string, "%b. %d, %Y")
    # Mengonversi objek datetime menjadi string dengan format yang diinginkan
    formatted_date = date_object.strftime("%Y-%m-%d")
    return formatted_date

def convert_to_dictionary(list_daftar_sponsor):
    #Converts a list of sponsors to a dictionary.
    dictionary = {}
    for row in list_daftar_sponsor:
        dictionary[row["id"]] = row["nama_brand"]
    return dictionary

# Create your views here.
def daftar_sponsor(request):
    user_id = get_current_user(request)["user_id"]
    result = query_result(f"""
                    SELECT s.nama_brand, s.id 
                    FROM sponsor s
                    WHERE NOT EXISTS (SELECT * FROM atlet_sponsor asp 
                                      WHERE s.id = asp.id_sponsor 
                                      AND asp.id_atlet = '{user_id}');
                """)
    list_sponsor = []  
    for row in result:
        list_sponsor.append({
            "id": row[0],
            "nama_brand": row[1],
        })

    list_daftar_sponsor = convert_to_dictionary(list_sponsor)
    # list_daftar_sponsor = {
    #     'daftar_sponsor': [
    #         {
    #             'id': 1,
    #             'nama_sponsor': 'Yonex',
    #         },
    #         {
    #             'id': 2,
    #             'nama_sponsor': 'Victor',
    #         },
    #         {
    #             'id': 3,
    #             'nama_sponsor': 'Li-Ning',
    #         },
    #     ]
    # }

    context = {
        "list_daftar_sponsor": list_daftar_sponsor,
        "role": get_current_user(request)["user_role"]
    }
    return render(request, 'daftar_sponsor.html', context)

@role_required(['ATLET'])
def form_daftar_sponsor(request):
    if (request.method == 'POST'):
        user_id = get_current_user(request)["user_id"]
        nama_sponsor = request.POST.get('nama_brand')
        id_sponsor = query_add(f"SELECT S.ID FROM SPONSOR S WHERE S.nama_brand ='{nama_sponsor}';")
        tanggal_mulai = request.POST.get('tanggal_mulai')
        tanggal_selesai = request.POST.get('tanggal_selesai')

        # HANDLE NONE FORM VALUE
        if (nama_sponsor == ''):
            context = {
                "send_data_is_valid": False
            }
            return render(request, 'form_daftar_sponsor.html', context)

        # INSERT DATA
        query_add(f"INSERT INTO atlet_sponsor VALUES ('{user_id}', '{id_sponsor}', '{tanggal_mulai}', '{tanggal_selesai}');")

        # REDIRECT
        response = HttpResponseRedirect(reverse("daftar_sponsor:form_daftar_sponsor"))
        return response
        
    context = {
        "send_data_is_valid": True
    }
    return render(request, 'form_daftar_sponsor.html', context)


@role_required(['ATLET'])
def list_daftar_sponsor(request):
    user_id = get_current_user(request)["user_id"]

    # GET DATA
    result = query_result(f"""SELECT nama_brand, tgl_mulai, tgl_selesai 
                FROM sponsor JOIN atlet_sponsor ON ID = ID_Sponsor
                WHERE ID_Atlet = '{user_id}';
                """)
    list_sponsor = []  
    for row in result:
        list_sponsor.append({
            "nama_brand": row[0],
            "tgl_mulai": row[1],
            "tgl_selesai": row[2],
        })
    context = {
        "list_sponsor": list_sponsor,
        "role": get_current_user(request)["user_role"]
    }
    return render(request, 'list_sponsor.html', context)