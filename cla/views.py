from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def computer(request):
    return render(request, 'computer.html')

def laptop(request):
    return render(request, 'laptop.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')

