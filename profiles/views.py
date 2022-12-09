from django.shortcuts import render, redirect

from .models import Profile
from .models import Skill

# New Login Inputs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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

# Search People

def searchPageView(request):
    context = {
            } 

    return render(request, 'profiles/search.html', context)

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


# Get Help with Skills

def searchSkillsView(request):
    context = {
            }

    return render(request, 'profiles/searchskills.html', context)


def findSkillsPageView(request):
    sSkill = (request.GET['skill']).upper()

    new_skill = Skill.objects.get(title=sSkill)
    data = Profile.objects.filter(skills=new_skill)

    return render(request, 'profiles/searchskills.html')



'''
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
'''

# NEW LOGIN
def loginPageView(request):
    return render(request, 'profiles/login.html')

'''
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')


    return render(request, "profiles/signup.html")
'''

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "profiles/index.html", {'fName':fname})

        else:
            messages.error(request, "Bad Credentials!")
            return HttpResponse('wrong password buddy')

    return render(request, "profiles/login.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('index')


# Profile
def profilePageView(request):
    if request.user.is_authenticated :
        new_person = request.user

        person = Profile.objects.get(user_name=new_person.username)

        fname = person.first_name
        lname = person.last_name
        phone = person.phone
        email = person.email

        username = person.user_name
        password = person.password
            



        data = {'fname': fname, 'lname' : lname, 'phone' : phone, 'email' : email, \
             'username' : username , 'password': password}

        context = {
            'profile' : data
        }

        return render(request, 'profiles/profile.html', context)

    else:
        return render(request, 'profiles/profile.html')

def storeProfilePageView(request):
    if request.user.is_authenticated :
        person = request.user

        new_person = Profile.objects.get(username=person.username)

        new_person.first_name = request.POST.get('fName')
        new_person.last_name = request.POST.get('lName')
        new_person.phone = request.POST.get('phone')
        new_person.email = request.POST.get('email')

        new_person.save()

        context = {
                'fName': request.POST.get('fName'), 
                'lName': request.POST.get('lName')
            }

        return render(request, 'profiles/index.html', context)

    else:
        if request.method == 'POST':
            new_person = Profile()

            new_person.first_name = request.POST.get('fName')
            new_person.last_name = request.POST.get('lName')
            new_person.phone = request.POST.get('phone')
            new_person.email = request.POST.get('email')

            new_person.user_name = request.POST.get('username')
            new_person.password = request.POST.get('pass1')
    

            new_person.save()

        
            username = request.POST['username']
            fname = request.POST['fName']
            lname = request.POST['lName']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            # if User.objects.filter(username=username):
            #     messages.error(request, "Username already exist! Please enter another username")
            #     return redirect('profile')
            
            # if User.objects.filter(email=email):
            #     messages.error(request, "Email already registered!")
            #     return redirect('profile')

            # if len(username)>10:
            #     messages.error(request, "Username must be under 10 characters")
            
            # if pass1 != pass2 :
            #     messages.error(request, "Passwords didn't match!")

            # if not username.isalnum():
            #     messages.error(request, "Username must include at least 1 letter")
            #     return redirect('profile')


            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            context = {
                'fName':fname, 
                'lName':lname
            }

    return render(request, 'profiles/index.html', context)