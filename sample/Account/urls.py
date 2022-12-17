from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('forgot/',views.forgot,name='forgot'),
    path('contacts/',views.contacts,name='contacts'),
    path('course/',views.course,name='course'),
    path('gallery/',views.gallery,name='gallery'),
    path('',views.mainhome,name='mainhome'),
   


]
