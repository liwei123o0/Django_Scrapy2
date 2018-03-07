# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_auto_20180306_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='net_spider',
            name='name',
            field=models.CharField(default='liwei', max_length=100),
        ),
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.CharField(primary_key=True, default=b'9f55496147ae4d9fbf39420ba69b2fa2', serialize=False,
                                   max_length=64, unique=True, verbose_name='uuid'),
        ),
    ]
