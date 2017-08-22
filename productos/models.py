# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=now)
    creator = models.ForeignKey(User,default=1)

class Image(models.Model):
    product = models.ForeignKey('Product',related_name='products_images', on_delete=models.CASCADE)
    owner = models.ForeignKey(User,default=1)
    photo = models.ImageField(upload_to = 'product_images/')
