from django.contrib import admin
from django.urls import path
from NewApp import views

urlpatterns = [
    path("",views.index, name="home"),
]
