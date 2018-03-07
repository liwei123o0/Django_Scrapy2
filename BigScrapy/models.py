# -*- coding: utf-8 -*-
# ! /usr/bin/env python

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Net_Spider(models.Model):
    id = models.UUIDField(verbose_name="uuid", primary_key=True, unique=True)
    create_by = models.CharField(verbose_name=u"创建者", max_length=100, default="", blank=True)
    create_date = models.DateField(verbose_name='创建时间', auto_now_add=True, blank=True)
    update_by = models.CharField(verbose_name=u"更新者", max_length=100, default="", blank=True)
    update_date = models.CharField(verbose_name=u"更新时间", max_length=100, default="", blank=True)
    remarks = models.CharField(verbose_name=u"备注信息", max_length=100, default="", blank=True)
    del_flag = models.CharField(verbose_name=u"逻辑标记", max_length=100, default="", blank=True)
    spider_name = models.CharField(verbose_name=u"爬虫名称", max_length=100, default="", blank=True)
    net_project_id = models.UUIDField(verbose_name=u"项目id", default="")
    allowed_domains = models.CharField(verbose_name=u"域名", max_length=100, default="", blank=True)
    proxy = models.BooleanField(verbose_name=u"代理", default=False)
    keywords = models.TextField(verbose_name=u"关键词插入", default="", blank=True)
    start_urls = models.TextField(verbose_name=u"入口连接", default="")
    spider_type = models.CharField(verbose_name=u"爬虫类型", max_length=50, default="")
    rules = models.CharField(verbose_name=u"规则入口", max_length=255, default="")
    fields = models.TextField(verbose_name=u"内容解析", default="")
    chinesename = models.CharField(verbose_name=u"网站名称", max_length=100, default="", blank=True)
    area_id = models.CharField(verbose_name=u"地域编码", max_length=100, default="", blank=True)
    tablename = models.CharField(verbose_name=u"表明", max_length=100, default="", blank=True)
    gen_gendbtable_id = models.CharField(verbose_name=u"关联表id", max_length=100, default="", blank=True)
    projectname = models.CharField(verbose_name=u"项目名称", max_length=100, default="", blank=True)
    keyword_type = models.CharField(verbose_name=u"关键字逻辑", max_length=100, default="", blank=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id
