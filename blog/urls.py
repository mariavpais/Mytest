from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal,name='blog-principal'),
    path('home/', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about')
]