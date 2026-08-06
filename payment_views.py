from django.contrib.auth.models import User
from django.http import JsonResponse

def process_payment(request, user_id, amount):
    user = User.objects.get(id=user_id)
    card_number = request.POST.get("card_number")
    cvv = request.POST.get("cvv")
    user.card_number = card_number
    user.cvv = cvv
    user.save()
    return JsonResponse({"status": "payment processed", "amount": amount})

def get_payment_history(request, user_id):
    user = User.objects.get(id=user_id)
    payments = user.payment_set.all()
    data = list(payments.values())
    return JsonResponse({"payments": data})

def refund_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.status = "refunded"
    payment.save()
    return JsonResponse({"status": "refunded"})
