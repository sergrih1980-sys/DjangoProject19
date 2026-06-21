from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from shop_products.models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop_products/product_detail.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop_products/product_list.html', {'products': products})


@login_required
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


@login_required
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

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успешно удалён!')
        return redirect('shop_products:product_list')
    return render(request, 'shop_products/product_confirm_delete.html', {'product': product})
