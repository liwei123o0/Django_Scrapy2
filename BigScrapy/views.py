# -*- coding: utf-8 -*-
# ! /usr/bin/env python

import uuid

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from BigScrapy.models import *


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    # 采集机管理数据
    Host_Project_Dict = Host_project.objects.filter(del_flag=1).values("host_name", "office_id", "ip_address",
                                                                       "project_name")

    Net_Spider_Dict = Net_Spider.objects.filter(del_flag=1, spider_type="news").values("spider_name", "chinesename",
                                                                                       "tablename", "area_id")

    Net_Spider_Search = Net_Spider.objects.filter(del_flag=1).exclude(spider_type="news").values("spider_name",
                                                                                                 "chinesename",
                                                                                                 "tablename", "area_id")

    dictdata = {"Host_Project_Dict": Host_Project_Dict, "Net_Spider_Dict": Net_Spider_Dict,
                "Net_Spider_Search": Net_Spider_Search}


    ### 图标时间解决  #####
    # dt = "20180501"
    # #转换成时间数组
    # timeArray = time.strptime(dt, "%Y%m%d")
    # #转换成时间戳
    # timestamp = time.mktime(timeArray)
    # 转换成13位时间戳
    # print int(timestamp) * 1000


    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(dictdata, request))


def add_jiqun(request):
    host_name = request.POST['host_name']
    ip_address = request.POST['ip_address']
    office_id = request.POST['office_id']
    project_name = request.POST['project_name']
    Host_project.objects.create(id=uuid.uuid4().hex, host_name=host_name, ip_address=ip_address,
                                office_id=office_id, project_name=project_name)
    return HttpResponseRedirect("app/hostproject.html")


def remove_jiqun(request):
    ip_address = request.POST['ip_address']
    Host_project.objects.filter(ip_address=ip_address).update(del_flag=0)
    return render(request, "app/hostproject.html")


def remove_spidername(request):
    spider_name = request.POST['spidername']
    Host_project.objects.filter(spider_name=spider_name).update(del_flag=0)
    return render(request, "app/newsspider.html")


def remove_search(request):
    spider_name = request.POST['spidername']
    Host_project.objects.filter(spider_name=spider_name).update(del_flag=0)
    return render(request, "app/searchspider.html")


def testindex(request):
    return render(request, 'app/test.html')
