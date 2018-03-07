# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.CharField(primary_key=True, default=b'02eeaa275240476a8645e74812e9fed7', serialize=False,
                                   max_length=64, db_tablespace=True, unique=True, verbose_name='uuid'),
        ),
    ]
