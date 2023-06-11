from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    # path('', views.team)
    ]
