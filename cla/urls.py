from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home', views.index),
    path('about', views.about),
    path('computer', views.computer),
    path('laptop', views.laptop),
    path('products', views.products),
    path('contact', views.contact),
]
