from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('home/base/', views.base, name='base'),
    path('home/about/', views.aboutpages, name='aboutpages'),
]
