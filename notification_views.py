from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.models import User

def notify_all_users(request, message):
    users = User.objects.filter(is_active=True)
    for user in users:
        send_mail(
            subject="Important notification",
            message=message,
            from_email="noreply@example.com",
            recipient_list=[user.email]
        )
    return JsonResponse({"status": "sent", "count": users.count()})

def send_welcome_email(request, user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        subject="Welcome",
        message=f"Hi {user.first_name}, welcome to our platform.",
        from_email="noreply@example.com",
        recipient_list=[user.email]
    )
    return JsonResponse({"status": "sent"})
