from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from babadu_function.authentication import *
from babadu_function.general import *

# Create your views here.

def latih_atlet(request):
    if get_current_user(request)["user_role"] == "PELATIH":
        result = query_result("SELECT m.id, nama FROM member m JOIN atlet a ON m.id = a.id;")

        daftar_atlet = {
            "daftar_atlet": []
        }

        for row in result:
            daftar_atlet["daftar_atlet"].append({
                "id_atlet": row[0],
                "nama_lengkap": row[1]
            })
        return render(request, 'latih_atlet.html', daftar_atlet)
    return HttpResponse('')

def submit_atlet(request):
    if request.method == "POST":
        try:
            user_id = get_current_user(request)["user_id"]
            id_atlet = request.POST.get('atlet')
            result = query_add(f"INSERT INTO atlet_pelatih VALUES ('{user_id}', '{id_atlet}');")
            return JsonResponse(0, safe=False)
        except:
            return JsonResponse(1, safe=False)
    return HttpResponse('')