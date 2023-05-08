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
  if request.method == "POST":
    email = request.POST.get("email")
    result = query_result(f"SELECT * FROM member WHERE email='{email}';")
    if len(result) != 0:
      print(result)
      print(role(result[0][0]))
    else:
      print("member not found")

  return render(request, 'login.html')

def logout(request):
  return render(request, 'logout.html')

def query_result(query):
  with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def role(member_id):
  result = query_result(f"SELECT * FROM umpire WHERE id='{member_id}';")
  if len(result) != 0:
    return "umpire"
  result = query_result(f"SELECT * FROM pelatih WHERE id='{member_id}';")
  if len(result) != 0:
    return "pelatih"
  result = query_result(f"SELECT * FROM atlet WHERE id='{member_id}';")
  if len(result) != 0:
    return "atlet"
  return "role for this member is not found"