from django.http import JsonResponse

from foodtaskerapp.models import Restaurant
from foodtaskerapp.serializers import RestaurantSerializer

# API function to retrieve restaurants data in Json
def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants": restaurants})