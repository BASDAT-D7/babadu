from django.shortcuts import render
from django.http import HttpResponse
from babadu_function.authentication import *
from babadu_function.general import *

# Create your views here.
def list_atlet_dilatih(request):
    if get_current_user(request)["user_role"] == "PELATIH":
        user_id = get_current_user(request)["user_id"]

        result = query_result(f'''
        SELECT nama, email, world_rank
        FROM atlet_pelatih ap
        JOIN member m ON ap.id_atlet = m.id
        JOIN atlet a ON ap.id_atlet = a.id
        WHERE ap.id_pelatih = '{user_id}';
        ''')

        list_atlet = {
            "list_atlet": []
        }

        for row in result:
            list_atlet["list_atlet"].append({
                "nama": row[0],
                "email": row[1],
                "world_rank": ("-" if row[2] == None else row[2])
            })
        return render(request, 'list_atlet_dilatih.html', list_atlet)
    return HttpResponse('')