# -*- coding: utf-8 -*-
# ! /usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index3.html')