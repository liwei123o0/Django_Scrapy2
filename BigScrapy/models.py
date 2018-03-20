# -*- coding: utf-8 -*-
# ! /usr/bin/env python

from __future__ import unicode_literals

from django.db import models


# 爬虫配置表
class Net_Spider(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    remarks = models.CharField(help_text=u"备注信息", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)
    spider_name = models.CharField(help_text=u"爬虫名称", max_length=100, default="", null=True)
    net_project_id = models.CharField(help_text=u"项目id", max_length=255, default="", null=True)
    allowed_domains = models.CharField(help_text=u"域名", max_length=100, default="", null=True)
    proxy = models.CharField(help_text=u"代理", max_length=100, default="false", null=True)
    keywords = models.TextField(help_text=u"关键词插入", default="", null=True)
    start_urls = models.TextField(help_text=u"入口连接", default="")
    spider_type = models.CharField(help_text=u"爬虫类型", max_length=50, default="")
    rules = models.CharField(help_text=u"规则入口", max_length=255, default="")
    fields = models.TextField(help_text=u"内容解析", default="")
    chinesename = models.CharField(help_text=u"网站名称", max_length=100, default="", null=True)
    area_id = models.CharField(help_text=u"地域编码", max_length=100, default="", null=True)
    tablename = models.CharField(help_text=u"表明", max_length=100, default="", null=True)
    gen_gendbtable_id = models.CharField(help_text=u"关联表id", max_length=100, default="", null=True)
    projectname = models.CharField(help_text=u"项目名称", max_length=100, default="", null=True)
    keyword_type = models.CharField(help_text=u"关键字逻辑", max_length=100, default="", null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id


# 数据定于表
class Gendbtable(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    dataclass_id = models.UUIDField(help_text="数据分类id", db_index=True, null=True)
    name = models.CharField(help_text=u"表名称", max_length=20, default="", null=True)
    comments = models.CharField(help_text=u"备注", max_length=50, default="", null=True)
    class_name = models.CharField(help_text=u"分类名称", max_length=50, default="", null=True)
    issync = models.BooleanField(help_text=u"是否同步", default=False)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id


# 数据字段定义表
class Gendbtable_column(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    gen_gendbtable_id = models.UUIDField(help_text="uuid", db_index=True, null=True)
    name = models.CharField(help_text=u"字段名称", max_length=20, default="", null=True)
    comments = models.CharField(help_text=u"备注", max_length=50, default="", null=True)
    field_type = models.CharField(help_text=u"字段类型", max_length=50, default="", null=True)
    data_len = models.IntegerField(help_text=u"字段长度", default=100, null=True)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id


# 数据主题类型表
class Data_class(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    net_spider_id = models.UUIDField(help_text="爬虫id", db_index=True, null=True)
    parent_id = models.CharField(help_text=u"父节点编号", max_length=32, default="", db_index=True, null=True)
    parent_ids = models.TextField(help_text=u"所有父节点编号", default="", null=True)
    name = models.CharField(help_text=u"名称", max_length=50, default="", null=True)
    sort = models.IntegerField(help_text=u"排序", default=30, null=True)
    code = models.CharField(help_text=u"数据编码", max_length=50, default="", null=True)
    data_len = models.IntegerField(help_text=u"字段长度", default=100, null=True)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id


# 爬虫集群配置表
class Host_project(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    office_id = models.CharField(help_text=u"归属部门", max_length=32, default="", null=True)
    ip_address = models.CharField(help_text=u"部署ip", max_length=32, default="", null=True)
    host_name = models.CharField(help_text=u"部署环境名称", max_length=32, default="", null=True)
    project_name = models.CharField(help_text=u"项目名称", max_length=50, default="", null=True)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="admin", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="admin", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id


# 关键字配置表
class Spider_keyword(models.Model):
    id = models.UUIDField(help_text="uuid", primary_key=True)
    dataclass_id = models.UUIDField(help_text="数据主题类型id", db_index=True, null=True)
    keyword = models.CharField(help_text=u"关键字", max_length=32, db_index=True, default="", null=True)
    keyword_type = models.CharField(help_text=u"关键字类型", max_length=32, default="", null=True)
    keyword_scene = models.CharField(help_text=u"应用场景", max_length=50, default="", null=True)
    create_by = models.CharField(help_text=u"创建者", max_length=100, default="", null=True)
    create_date = models.DateField(help_text='创建时间', auto_now_add=True, null=True)
    update_by = models.CharField(help_text=u"更新者", max_length=100, default="", null=True)
    update_date = models.CharField(help_text=u"更新时间", max_length=100, default="", null=True)
    del_flag = models.IntegerField(help_text=u"逻辑标记", default=1, null=True)

    def __unicode__(self):  # __str__ on Python 3
        return self.id
