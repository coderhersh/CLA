from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


def products(request):

    p1 = Product()
    p1.title = 'Computer'
    p1.image = 'leptop.jpg'
    p1.description = 'This is the latest version AMD CPU Computer'
    p1.price = 4000.0
    p1.discount = 0.0

    p2 = Product()
    p2.title = 'RAM'
    p2.image = 'product2.png'
    p2.description = 'This is the latest version AMD CPU Computer'
    p2.price = 7845.0
    p2.discount = 45.0

    p3 = Product()
    p3.title = 'CPU'
    p3.image = 'product3.png'
    p3.description = 'This is the latest version AMD CPU Computer'
    p3.price = 4500.0
    p3.discount = 10.0
    
    p4 = Product()
    p4.title = 'Mouse'
    p4.image = 'product4.png'
    p4.description = 'This is the latest version AMD CPU Computer'
    p4.price = 4500.0
    p4.discount = 10.0

    products = [p1, p2, p3, p4]
    return render(request, 'products.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def computer(request):
    return render(request, 'computer.html')

def laptop(request):
    return render(request, 'laptop.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def facebook(request):
    return redirect('www.facebook.com')