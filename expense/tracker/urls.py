from django.contrib import admin
from django.urls import path
from tracker.views import *

urlpatterns = [
    path('',index),
]