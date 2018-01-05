# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from forms import RotaluclacForm
from rotaluclac.calculate import *
from rotaluclac.exceptions import UnsolvableEquationError


def index(request):
    return render(request, 'index/index.html')

def projects(request):
    if request.method == 'POST':
        form = RotaluclacForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            equation = cd['equation']
            base = cd['base']
            notation = cd['notation']
            try:
                result = ""
                if notation == "polish":
                    result = solvePostFix(equation)
                else:
                    result = solveInFix(equation)
                if base == 'binary':
                    result = '0b' + str(int(result,2))
                elif base == 'octal':
                    result = '0o' + str(int(result,8))
                elif base == 'hexadecimal':
                    result = '0x' + str(int(result,16))
                return render(request, 'index/projects.html', {'result': result, 'form':form})
            except UnsolvableEquationError as error:
                return render(request, 'index/projects.html', {'form':form, 'error':error})

    else:
        form = RotaluclacForm()
    return render(request, 'index/projects.html', {'form':form})

def contact(request):
    return render_to_response(request, 'index/contact.html')
