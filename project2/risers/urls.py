from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('myhome/', views.myhome, name="myhome"),
    path('signup/', views.sign_up,name="sign_up"),
    path('home/', views.home,name="home"),
    path('login/', views.mylogin,name="mylogin"),
    path('logout/', views.mylogout, name="mylogout"),

]