from babadu_function.general import query_result

def role(member_id):
    result = query_result(f"SELECT * FROM umpire WHERE id='{member_id}';")
    if len(result) != 0:
        return "UMPIRE"
    result = query_result(f"SELECT * FROM pelatih WHERE id='{member_id}';")
    if len(result) != 0:
        return "PELATIH"
    result = query_result(f"SELECT * FROM atlet WHERE id='{member_id}';")
    if len(result) != 0:
        return "ATLET"
    return "NONE"

def is_authenticated(request):
    if request.COOKIES.get('is_authenticated') == "True":
        return True
    return False

def get_current_user(request):
    user_id = request.COOKIES.get('user_id')
    user_role = request.COOKIES.get('user_role')
    context = {
        'user_id': user_id,
        'user_role': user_role,
    }
    return context