# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from productos.models import Product,Image
from productos.serializers import ProductSerializer,ImageSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
