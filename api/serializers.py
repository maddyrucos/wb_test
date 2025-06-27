from rest_framework import serializers, viewsets
from wb_parser.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'