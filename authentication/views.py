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
  return render(request, 'register_form/register_atlet.html')

def register_pelatih(request):
  return render(request, 'register_form/register_pelatih.html')

def register_umpire(request):
  if request.method == "POST":
    user_id = uuid.uuid4()
    nama = request.POST.get("nama")
    email = request.POST.get("email")
    negara = request.POST.get("negara")
    query_add(f"INSERT INTO member (id, nama, email) VALUES ('{user_id}', '{nama}', '{email}');")
    query_add(f"INSERT INTO umpire (id, negara) VALUES ('{user_id}', '{negara}')")
  return render(request, 'register_form/register_umpire.html')

def login(request):
  if request.method == "POST":
    email = request.POST.get("email")
    result = query_result(f"SELECT * FROM member WHERE email='{email}';")
    if len(result) != 0:
      user_id = result[0][0]
      user_role = role(result[0][0])
      response = HttpResponseRedirect(reverse("dashboard:dashboard"))
      # SET COOKIES
      response.set_cookie('user_id', user_id)
      response.set_cookie('user_role', user_role)
      response.set_cookie('is_authenticated', True)
      return response
    else:
      print("MEMBER NOT FOUND")
  return render(request, 'login.html')

def logout(request):
  response = HttpResponseRedirect(reverse('authentication:login'))
  response.delete_cookie('user_id')
  response.delete_cookie('user_role')
  response.delete_cookie('is_authenticated')
  return response

