from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    category_url = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category_url)
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product_url = Product.objects.get(slug=slug)
    context = {
        'product': product_url
    }
    return render(request, 'catalog/product.html', context)




