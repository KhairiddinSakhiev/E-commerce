import django_filters
from .models import *



# class ProductFilter(django_filters.FilterSet):
#     price = django_filters.RangeFilter()

#     class Meta:
#         model = Product
#         fields = {
#         'product_title': ['istartwith']
#         }

class ProductFilter(django_filters.FilterSet):
    product_title = django_filters.CharFilter(field_name='product_title', lookup_expr='icontains')
    product_region = django_filters.CharFilter(field_name='product_region', lookup_expr='icontains')
    product_price = django_filters.RangeFilter(field_name='product_price')

    class Meta:
        model = Product
        fields = {'product_title', 
                  'product_region', 
                  'product_price',
                  }