from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def menu(request):
    return render(request, 'home/menu.html')

def administration(request):
    return render(request, 'home/administration.html')

def contact(request):
    return render(request, 'home/contact.html')
