# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Hello World')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def produtct(request):
    return render(request, 'product.html')



