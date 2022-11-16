from django.shortcuts import render

from .models import Profile
from .models import Skill

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
    data = Profile.objects.all()

    context = {
        "our_profiles" : data
    }

    return render(request, 'profiles/display.html', context)

def inputPageView(request):
    data_skill = Skill.objects.all()

    context = {
        "our_skills" : data_skill
    }

    return render(request, 'profiles/input.html', context)

def searchPageView(request):
    context = {
            } 

    return render(request, 'profiles/search.html', context)

def searchProfilePageView(request):
    context = {
            } 

    return render(request, 'profiles/search.html', context)

def findProfilePageView(request):
    return render(request, 'profiles/search.html')

def searchProfilePageView(request) :
    sFirst = (request.GET['first_name']).upper()
    sLast = (request.GET['last_name']).upper()
    data = Profile.objects.filter(first_name=sFirst, last_name=sLast)

    if data.count() > 0:
        context = {
            "our_profiles" : data
        }
        return render(request, 'profiles/display.html', context)
    else:
        return HttpResponse("Not found")

def inputProfilePageView(request):
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        profile = Profile()
        
        #Store the data from the form to the new object's attributes (like columns)
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.user_name = request.POST.get('user_name')
        profile.password = request.POST.get('password')
        profile.phone = request.POST.get('phone')
        profile.email = request.POST.get('email')

        #new_skill = Skill.objects.get(id = request.POST.get('id'))
        new_skill = request.POST.get('skills.id')

        profile.skills.add(Skill.object.get(id = new_skill))
        
        profile.save()
        
    data = Profile.objects.all()

    context = {
        "our_profiles" : data
    }
    return render(request, 'profiles/display.html', context) 