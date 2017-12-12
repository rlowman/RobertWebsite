# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from forms import RotaluclacForm


def index(request):
    return render(request, 'index/index.html')

def projects(request):
    if request.method == 'POST':
        form = RotaluclacForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            equation = cd['equation']
            result = equation + "$"
            return render(request, 'polls/projects.html', {'result': result, 'form':form})
    else:
        form = RotaluclacForm()
    return render(request, 'polls/projects.html', {'form':form})

def contact(request):
    return render_to_response(request, 'polls/contact.html')
