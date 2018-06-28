# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .forms import RotaluclacForm, SodokuBoard
from .projects.calculate import *
from .projects.sodoku import solveBacktracking
from .projects.exceptions import UnsolvableEquationError

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
                    return render(request, 'index/projects.html', {'result': result, 'rotForm':rotForm, 'board':board, 'error':error})
        elif "sodoku" in request.POST:
            board = SodokuBoard(request.POST)
            board.is_valid():
            temp = readBoard(board)
            try:
                data = solveBacktracking(temp)
                board = writeBoard(data)
                return render(request, 'index/projects.html', {'rotForm':rotForm, 'board':board})
            except UnsolvableEquationError as sodokuError:
                return render(request, 'index/projects.html', {'rotForm':rotForm, 'board':board, 'sodokuError':sodokuError})
    else:
        form = RotaluclacForm()
    return render(request, 'index/projects.html', {'rotForm':rotForm, 'board':board})

def contact(request):
    return render(request, 'index/contact.html')

def about(request):
    return render(request, 'index/about.html')

def readBoard(board):
    returnValue = []
    if board.is_valid():
        for row in range(9):
            for col in range(9):
                getString = 'cellRow' + str(row) + 'Col' + str(col)
                temp = board.cleaned_data[getString]
                if len(temp) > 0:
                    returnValue.append(temp)
                else:
                    returnValue.append(0)
    return returnValue

def writeBoard(data):
    returnBoard = SodokuBoard()
    for row in range(9):
        for col in range(9):
            getString = "cellRow" + str(row) + "Col" + str(col)
            index = (row * 9) + col
            returnBoard.fields[getString].initial = data.get(str(row + 1) + str(col + 1))
    return returnBoard
