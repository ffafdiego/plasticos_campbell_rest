# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=now)
    photo = models.ImageField(upload_to = 'products/')
