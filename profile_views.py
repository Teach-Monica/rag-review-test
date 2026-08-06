from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

class UserProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return JsonResponse({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_staff": user.is_staff,
            "password": user.password
        })

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        return JsonResponse({"status": "updated"})

    def delete(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({"status": "deleted"})
