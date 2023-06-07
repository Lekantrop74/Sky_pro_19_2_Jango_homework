from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'catalog/home_page.html')


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contact.html')
