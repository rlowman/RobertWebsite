# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from forms import RotaluclacForm, SodokuBoard
from projects.calculate import *
from projects.exceptions import UnsolvableEquationError


def index(request):
    return render(request, 'index/index.html')

def projects(request):
    emptyBoard = [[None]*9 for _ in range(9)]
    rotForm = RotaluclacForm()
    board = SodokuBoard()
    if request.method == 'POST':
        if "polish_notation" in request.POST:
            rotForm = RotaluclacForm(request.POST)
            if rotForm.is_valid():
                cd = rotForm.cleaned_data
                equation = cd['equation']
                base = cd['base']
                notation = cd['notation']
                try:
                    result = ""
                    if notation == "polish":
                        result = solveInFix(equation)
                    else:
                        result = solvePostFix(equation)
                    if base == 'binary':
                        result = '0b' + str(int(result,2))
                    elif base == 'octal':
                        result = '0o' + str(int(result,8))
                    elif base == 'hexadecimal':
                        result = '0x' + str(int(result,16))
                    return render(request, 'index/projects.html', {'result': result, 'rotForm':rotForm, 'board':board})
                except UnsolvableEquationError as error:
                    return render(request, 'index/projects.html', {'result': result, 'rotForm':rotForm, 'board':board})
        elif "sodoku" in request.POST:
            board = SodokuBoard(request.POST)
            if board.is_valid():
                alg = board.cleaned_data['algorithm']
                data = solveBoard(board)
                board = writeBoard(data)
                return render(request, 'index/projects.html', {'rotForm':rotForm, 'board':board})
    else:
        form = RotaluclacForm()
    return render(request, 'index/projects.html', {'rotForm':rotForm, 'board':board})

def contact(request):
    return render_to_response(request, 'index/contact.html')
