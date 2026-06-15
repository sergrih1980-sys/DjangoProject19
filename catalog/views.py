from django.views.generic import TemplateView, DetailView, ListView
from django.contrib import messages
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


class ContactsView(TemplateView):
    template_name = "contacts.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Продукт "{product.name}" успешно создан!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Создание продукта'
    })

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save()
            messages.success(request, f'Продукт "{updated_product.name}" успешно обновлён!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': f'Редактирование продукта: {product.name}',
        'product': product
    })

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, f'Продукт "{product.name}" успешно удалён!')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

