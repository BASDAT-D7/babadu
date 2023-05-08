from django.shortcuts import render
from django.db import connection

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
  return render(request, 'register_form/register_umpire.html')

def login(request):
  with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM member;")
      members = cursor.fetchall()

      print(members)

  return render(request, 'login.html')

def logout(request):
  return render(request, 'logout.html')