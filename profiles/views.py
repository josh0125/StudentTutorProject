from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Home Page') 

def aboutPageView(request) :
    return HttpResponse('About Page') 

def displayPageView(request) :
    return HttpResponse('Display Page') 

def inputPageView(request):
    return HttpResponse('Input Page')

def searchPageView(request):
    return HttpResponse('Search Page')
