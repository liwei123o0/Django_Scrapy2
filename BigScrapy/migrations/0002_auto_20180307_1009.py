# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BigScrapy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='net_spider',
            name='name',
            field=models.CharField(default='liwei', max_length=100, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='net_spider',
            name='id',
            field=models.UUIDField(unique=True, serialize=False, verbose_name='uuid', primary_key=True),
        ),
    ]
