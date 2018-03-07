# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0006_auto_20180306_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.UUIDField(primary_key=True, default=b'6218f31827e149899929ac4b496806c9', serialize=False,
                                   unique=True, verbose_name='uuid'),
        ),
    ]
