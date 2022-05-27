from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('computer', views.computer, name='computer'),
    path('laptop', views.laptop, name='laptop'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
]
