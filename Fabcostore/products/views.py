from django.shortcuts import render,redirect

from .models import Product


# Create your views here.


def index(request):

    products = Product.objects.all()
    return render(request,'index.html', {'products' : products} )


def shop(request):

    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})



def detail(request):
    return render(request,'detail.html')


def contact(request):
    return render(request, 'contact.html')


