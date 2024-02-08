from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("home",views.home,name="home"),
    path("forntend",views.forntend,name="forntend"),

    #signup validation url 
    path("Signup",views.handleSignup,name="handleSignup"),


    #Login validation url 
    path("Login",views.handleLogin,name="handleLogin"),


    #Logout validation url 
    path("Logout",views.handleLogout,name="handleLogout"),
    

    #online editor
    path("onlineeditor",views.onlineeditor,name="editor"),

    # HTML forntend course
    path("html1",views.html1,name="forntend"),
    path("htmlvideo",views.htmlvideo,name="htmlvideo"),
    #CSS forntend Course
    path("css1",views.css1,name='css1'),
    path("signuptest",views.signuptest,name="signuptest"),
    # news letter subscipttion is here 
    path("newsletter",views.newsletter,name='newsletter')
]

