from django.contrib.auth.models import User

def get_user_profile(user_id):
    user = User.objects.get(id=user_id)
    return {
        "name": user.get_full_name(),
        "email": user.email,
        "joined": user.date_joined
    }

def deactivate_user(user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
