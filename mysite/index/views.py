# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from forms import RotaluclacForm
from rotaluclac.calculate import *
from rotaluclac.exceptions import InvalidSymbolError, InvalidNumberFormat, InvalidEquationError


def index(request):
    return render(request, 'index/index.html')

def projects(request):
    if request.method == 'POST':
        form = RotaluclacForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            equation = cd['equation']
            try:
                result = solve(equation)
                return render(request, 'index/projects.html', {'result': result, 'form':form})
            except InvalidSymbolError:
                # TODO error message
                return HttpResponse("Error")
            except InvalidNumberFormat:
                # TODO error message
                return HttpResponse("Error")
            except InvalidEquationError:
                # TODO error message
                return HttpResponse("error")
    else:
        form = RotaluclacForm()
    return render(request, 'index/projects.html', {'form':form})

def contact(request):
    return render_to_response(request, 'index/contact.html')
