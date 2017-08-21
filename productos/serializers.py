from rest_framework import serializers
from productos.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'nick', 'quantity', 'pub_date', 'photo')
