import django_filters
from wb_parser.models import Product

class ProductFilter(django_filters.FilterSet):
    nm_id = django_filters.NumberFilter(field_name="nm_id", lookup_expr="exact")
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    price_basic_min = django_filters.NumberFilter(field_name="price_basic", lookup_expr="gte")
    price_basic_max = django_filters.NumberFilter(field_name="price_basic", lookup_expr="lte")

    price_basic_rub_min = django_filters.NumberFilter(field_name="price_basic_rub", lookup_expr="gte")
    price_basic_rub_max = django_filters.NumberFilter(field_name="price_basic_rub", lookup_expr="lte")

    price_total_min = django_filters.NumberFilter(field_name="price_total", lookup_expr="gte")
    price_total_max = django_filters.NumberFilter(field_name="price_total", lookup_expr="lte")

    price_total_rub_min = django_filters.NumberFilter(field_name="price_total_rub", lookup_expr="gte")
    price_total_rub_max = django_filters.NumberFilter(field_name="price_total_rub", lookup_expr="lte")

    rating_min = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    rating_max = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")

    feedbacks_min = django_filters.NumberFilter(field_name="feedbacks", lookup_expr="gte")
    feedbacks_max = django_filters.NumberFilter(field_name="feedbacks", lookup_expr="lte")

    class Meta:
        model = Product
        fields = [
            'nm_id', 'name',
            'price_basic_min', 'price_basic_max',
            'price_basic_rub_min', 'price_basic_rub_max',
            'price_total_min', 'price_total_max',
            'price_total_rub_min', 'price_total_rub_max',
            'rating_min', 'rating_max',
            'feedbacks_min', 'feedbacks_max',
        ]