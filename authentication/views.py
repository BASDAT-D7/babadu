from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from babadu_function.general import *
from babadu_function.authentication import *
import uuid

# Create your views here.
def authentication(request):
  return render(request, 'authentication.html')

def register(request):
  return render(request, 'register.html')

def register_atlet(request):
  if request.method == "POST":
    # GET DATA
    user_id = uuid.uuid4()
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    negara = request.POST.get("negara")
    tanggal_lahir = request.POST.get("tanggal_lahir")
    tinggi_badan = request.POST.get("tinggi_badan")
    jenis_kelamin = request.POST.get("jenis_kelamin")
    play = request.POST.get("play")

    # INSERT DATA
    try:
      query_add(f"INSERT INTO member (id, nama, email) VALUES ('{user_id}', '{nama}', '{email}');")
      query_add(f"INSERT INTO atlet (id, tgl_lahir, negara_asal, play_right, height, world_rank, jenis_kelamin) VALUES ('{user_id}', '{tanggal_lahir}', '{negara}', {play}, {tinggi_badan}, NULL, {jenis_kelamin});")  

      # REDIRECT
      response = HttpResponseRedirect(reverse("dashboard:dashboard"))
      print(response)
      return response
    except:
      context = {
        "is_email_exist": True
      }
      return render(request, 'register_form/register_atlet.html', context)

  context = {
    "is_email_exist": False
  }
  return render(request, 'register_form/register_atlet.html', context)

def register_pelatih(request):
  if request.method == "POST":
    # GET DATA
    user_id = uuid.uuid4()
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    negara = request.POST.get("negara")
    tanggal_mulai = request.POST.get("tanggal_mulai")
    kategori = request.POST.get("kategori")
    
    try:
      # INSERT DATA
      query_add(f"INSERT INTO member (id, nama, email) VALUES ('{user_id}', '{nama}', '{email}');")
      query_add(f"INSERT INTO pelatih (id, tanggal_mulai) VALUES ('{user_id}', '{tanggal_mulai}');");
      query_add(f"INSERT INTO pelatih_spesialisasi (id_pelatih, id_spesialisasi) VALUES ('{user_id}', '{kategori}');")
    
      # REDIRECT
      response = HttpResponseRedirect(reverse("dashboard:dashboard"))
      return response
    except:
      context = {
        "is_email_exist": True
      }
      return render(request, 'register_form/register_pelatih.html', context)

  context = {
    "is_email_exist": False
  }
  return render(request, 'register_form/register_pelatih.html', context)

def register_umpire(request):
  if request.method == "POST":
    # GET DATA
    user_id = uuid.uuid4()
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    negara = request.POST.get("negara")
    
    try:
      # INSERT DATA
      query_add(f"INSERT INTO member (id, nama, email) VALUES ('{user_id}', '{nama}', '{email}');")
      query_add(f"INSERT INTO umpire (id, negara) VALUES ('{user_id}', '{negara}')")
      
      # REDIRECT
      response = HttpResponseRedirect(reverse("dashboard:dashboard"))
      return response
    except:
      context = {
        "is_email_exist": True
      }
      return render(request, 'register_form/register_umpire.html', context)

  context = {
    "is_email_exist": False
  }
  return render(request, 'register_form/register_umpire.html', context)

def login(request):
  context = {"error": ""}
  if request.method == "POST":
    # GET DATA
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    result = query_result(f"SELECT * FROM member WHERE nama='{nama}' AND email='{email}';")
    print(result)
    
    if len(result) != 0:
      user_id = result[0][0]
      user_role = role(result[0][0])
      response = HttpResponseRedirect(reverse("dashboard:dashboard"))
      
      # SET COOKIES
      response.set_cookie('user_id', user_id)
      response.set_cookie('user_role', user_role)
      response.set_cookie('is_authenticated', "True")
      
      # REDIRECT
      return response
    else:
      context = {"is_error": True}

  return render(request, 'login.html', context)

def logout(request):
  # DELETE COOKIES
  response = HttpResponseRedirect(reverse('authentication:authentication'))
  response.delete_cookie('user_id')
  response.delete_cookie('user_role')
  response.delete_cookie('is_authenticated')

  return response

