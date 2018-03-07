# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_auto_20180306_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.CharField(primary_key=True, default=b'c8305bdcdad24071bf3af4f5848f0c50', serialize=False,
                                   max_length=64, unique=True, verbose_name='uuid'),
        ),
    ]
