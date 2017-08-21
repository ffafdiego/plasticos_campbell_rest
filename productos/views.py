# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from productos.models import Product
from productos.serializers import ProductSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
