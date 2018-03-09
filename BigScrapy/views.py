# -*- coding: utf-8 -*-
# ! /usr/bin/env python

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from BigScrapy.models import *


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):

    dictdata = {}

    datadict()
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


def datadict():
    pass
    # for i in range(10, 100, 1):
    #     print "##%s##" % i
    #     Net_Spider.objects.create(name="aaa%s" % i, id=uuid.uuid4().hex)


def add_jiqun(request):
    host_name = request.GET['host_name']
    ip_address = request.GET['ip_address']
    office_id = request.GET['office_id']
    project_name = request.GET['project_name']
    Host_project.objects.create(id=uuid.uuid4().hex, host_name=host_name, ip_address=ip_address,
                                office_id=office_id, project_name=project_name)

    return render(request, "app/hostproject.html")


if __name__ == '__main__':
    print uuid.uuid4().hex
