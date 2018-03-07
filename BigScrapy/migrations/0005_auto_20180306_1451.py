# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0004_auto_20180306_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.CharField(primary_key=True, default=b'56ceaf914ebd48309f187dcedf526426', serialize=False,
                                   max_length=64, unique=True, verbose_name='uuid'),
        ),
    ]
