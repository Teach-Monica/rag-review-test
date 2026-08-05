from django.contrib.auth.models import User
from django.http import JsonResponse

def get_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({
        "name": user.get_full_name(),
        "email": user.email,
        "joined": str(user.date_joined)
    })

def reset_user_password(request, user_id):
    user = User.objects.get(id=user_id)
    new_password = request.POST.get("password")
    user.password = new_password
    user.save()
    return JsonResponse({"status": "password updated"})

def deactivate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return JsonResponse({"status": "deactivated"})
