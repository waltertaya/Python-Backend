from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import JsonResponse

from products.serializers import ProductSerializer
from products.models import Product


@api_view(["GET", "POST"])
def product(request, *args, **kwargs):
    if request.method == 'GET':
        instance = Product.objects.all().order_by('?').first()

        data = {}
        if instance:
            # data['id'] = products.id
            # data['title'] = products.title
            # data['description'] = products.description
            # data['price'] = products.price
            # data['sale_price'] = products.sale_price
            data = ProductSerializer(instance).data

        return Response(data)
    
    else:
        if isinstance(request.data, list):
            serialized = ProductSerializer(data=request.data, many=True)
        else:
            serialized = ProductSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        
@api_view(["GET"])
def all_products(requests, *args, **kwargs):
    instance = Product.objects.all()
    data = {}
    if instance:
        data = ProductSerializer(instance, many=True).data

    return Response(data)
