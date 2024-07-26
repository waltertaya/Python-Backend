from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import JsonResponse

from products.serializers import ProductSerializer
from products.models import Product


@api_view(["GET"])
def index(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()

    data = {}
    if instance:
        # data['id'] = products.id
        # data['title'] = products.title
        # data['description'] = products.description
        # data['price'] = products.price
        # data['sale_price'] = products.sale_price
        print(instance.title)
        data = ProductSerializer(instance).data

    return Response(data)
