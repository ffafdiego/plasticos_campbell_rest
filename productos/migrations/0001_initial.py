# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nick', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('photo', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
