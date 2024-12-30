from django.shortcuts import render, redirect
from .models import Product
from .form import ProductModelForm


def home_view(request):
    return render(request, 'Assets/home.html')

def product_create_view(request):
    form = ProductModelForm()
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'Assets/product_form.html', {'form': form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'Assets/product_list.html', {'products': products})

def product_update_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    form = ProductModelForm(instance=product)
    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'Assets/product_form.html', {'form': form})

def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'Assets/product_delete.html', {'product': product})
        
