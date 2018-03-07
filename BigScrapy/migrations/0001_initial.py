# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Net_Spider',
            fields=[
                ('id', models.CharField(primary_key=True, default=b'b516e27f2cb647ef8c37fd06b0d1a0b4', serialize=False,
                                        max_length=64, db_tablespace=True, unique=True, verbose_name='uuid')),
            ],
        ),
    ]
