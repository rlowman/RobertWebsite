# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'polls/index.html')

def projects(request):
    if request.method == 'POST':
        equation = request.POST.get('textfield', None)
        result = equation + "$"
        return render(request, 'polls/projects.html', {'result': result})
    else:
        return render(request, 'polls/projects.html')

def contact(request):
    return render(request, 'polls/contact.html')
