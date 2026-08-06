from django.contrib.auth.models import User
from django.http import JsonResponse

def get_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({
        "username": user.username,
        "email": user.email,
        "password": user.password
    })

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return JsonResponse({"status": "deleted"})
