from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from wb_parser.models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
