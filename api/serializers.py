from rest_framework import serializers, viewsets
from wb_parser.models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount_percent = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'nm_id', 'name',
            'price_basic_rub', 'price_total_rub',
            'rating', 'feedbacks',
            'discount_percent',
        ]

    def get_discount_percent(self, obj):
        if obj.price_basic_rub == 0:
            return 0
        return round((obj.price_basic_rub - obj.price_total_rub) / obj.price_basic_rub * 100, 2)
