from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm
# Create your views here.

def index(request):
    return render(request, "store_app/base.html")

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store_app/products_list.html", context=context)


def product(request, id: int):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "store_app/product.html", context=context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            category = Category.objects.first()
            Product.objects.create(name=name, description=description, price=price, category=category)
            return redirect('products_list')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'title': 'Добавление товара'
    }
    return render(request, 'store_app/add_product.html', context=context)


def edit_product(request, id_product):
    product = get_object_or_404(Product, pk=id_product)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.save()
            return redirect('products_list')
    else:
        form = ProductForm(initial={
            'name': product.name,
            'price': product.price,
            'description': product.description,
        })

    context = {
        'form': form,
        'title': 'Изменение продукта'
    }
    return render(request, 'store_app/edit_product.html', context=context)

