from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def indexPageView(request) :
    context = {
           } 
    
    return render(request, 'profiles/index.html', context)

def aboutPageView(request) :
    context = {
            } 

    return render(request, 'profiles/about.html', context)

def displayPageView(request) :
    context = {
            } 

    return render(request, 'profiles/display.html', context)

def inputPageView(request):
    context = {
            } 

    return render(request, 'profiles/input.html', context)

def searchPageView(request):
    context = {
            } 

    return render(request, 'profiles/search.html', context)
