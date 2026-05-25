from django.shortcuts import render, get_object_or_404
from .models import Product


def contacts(request):
    return render(request, "contacts.html")

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)

