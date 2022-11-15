from django.urls import path

from .views import indexPageView
from .views import aboutPageView
from .views import displayPageView
from .views import inputPageView
from .views import searchPageView



urlpatterns = [
    path("", indexPageView, name="index"),    

    path("about", aboutPageView, name="about"),   

    path("display", displayPageView, name="display"),  

    path("input", inputPageView, name="input"), 

    path("search", searchPageView, name="search"),
]   

