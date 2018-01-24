# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User


# get your views here.

def index(request):

    return render(request, 'index.html')

def Users(request):
    if request.method =='GET':
        user=User(request.GET)

        data=User.objects.all()
        print "print all data"

    return render(request, 'success.html', {'data': data})

