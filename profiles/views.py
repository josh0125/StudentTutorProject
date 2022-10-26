from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Team!') 
