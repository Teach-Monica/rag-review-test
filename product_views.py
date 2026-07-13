from django.http import JsonResponse
from shop.models import Product, Review

def get_all_products(request):
    products = Product.objects.all()
    data = list(products.values())
    return JsonResponse({"products": data})

def get_product_reviews(request, product_id):
    reviews = Review.objects.filter(product_id=product_id).order_by("-created_at")
    data = list(reviews.values())
    return JsonResponse({"reviews": data})
