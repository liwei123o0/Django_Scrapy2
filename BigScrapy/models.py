# -*- coding: utf-8 -*-
# ! /usr/bin/env python

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Net_Spider(models.Model):
    id = models.UUIDField(u"uuid", primary_key=True, max_length=64, unique=True)
    name = models.CharField(u"姓名", max_length=100, default="liwei")

    def __unicode__(self):  # __str__ on Python 3
        return self.id
