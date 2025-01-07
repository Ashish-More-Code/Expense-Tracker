from django.contrib import admin
from django.urls import path
from tracker.views import *

urlpatterns = [
    path('',index),
    path('register/',rigistration,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logot_user,name='logout'),
    path('delete-transaction/<uid>',deleteTransaction,name="deleteTransaction")
]