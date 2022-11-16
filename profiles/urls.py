from django.urls import path

from .views import indexPageView
from .views import aboutPageView
from .views import displayPageView
from .views import inputPageView
from .views import searchPageView
from .views import inputProfilePageView
from .views import searchProfilePageView
from .views import findProfilePageView


urlpatterns = [
    path("", indexPageView, name="index"),    

    path("about", aboutPageView, name="about"),   

    path("display/", displayPageView, name="display"),  

    path("input", inputPageView, name="input"), 

    path("search", searchPageView, name="search"),

    path("searchprofile/", searchProfilePageView, name="searchprofile"),
    
    path("findprofile/", findProfilePageView, name="findprofile"),

    path("inputprofile/", inputProfilePageView, name="inputprofile"),


]   

