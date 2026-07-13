from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.cache import cache

def get_user_dashboard(request, user_id):
    user = User.objects.get(id=user_id)
    orders = list(user.order_set.all().values())
    recent_activity = list(user.activity_set.order_by("-created_at").values())
    notifications = list(user.notification_set.filter(read=False).values())
    return JsonResponse({
        "user": {"name": user.get_full_name(), "email": user.email},
        "orders": orders,
        "recent_activity": recent_activity,
        "notifications": notifications
    })

def update_user_settings(request, user_id):
    user = User.objects.get(id=user_id)
    data = request.POST
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user.email = data.get("email", user.email)
    user.save()
    return JsonResponse({"status": "updated"})
