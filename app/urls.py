from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('about/', views.about, name='about'),
    path('weather/', views.weather, name='weather'),
]