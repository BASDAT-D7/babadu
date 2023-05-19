from babadu_function.general import query_result
from functools import wraps
from django.http import HttpResponseForbidden

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

# Decorator untuk memberi permission
def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            user_role = request.COOKIES.get('user_role')  # Ambil peran dari cookie

            if user_role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Unauthorized access")

        return wrapped_view

    return decorator