# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0005_auto_20180306_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.CharField(primary_key=True, default=b'98cf330a800140dc88dc8e66970186c8', serialize=False,
                                   max_length=64, unique=True, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='net_spider',
            name='name',
            field=models.CharField(default='liwei', max_length=100, verbose_name='\u59d3\u540d'),
        ),
    ]
