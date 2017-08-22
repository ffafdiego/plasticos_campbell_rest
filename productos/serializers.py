from rest_framework import serializers
from productos.models import Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','product', 'owner', 'photo')



class ProductSerializer(serializers.ModelSerializer):
    # products_images = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='id'
    #  )
    products_images = ImageSerializer(
        many=True
     )
    class Meta:
        model = Product
        fields = ('id', 'name', 'nick', 'quantity','creator','products_images')
