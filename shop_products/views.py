from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop_products.models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop_products/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан!')
            return redirect('shop_products:product_list')
    else:
        form = ProductForm()
    return render(request, 'shop_products/product_form.html', {'form': form, 'title': 'Создать продукт'})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлён!')
            return redirect('shop_products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop_products/product_form.html', {'form': form, 'title': 'Редактировать продукт'})