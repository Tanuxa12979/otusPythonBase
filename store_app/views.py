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
    #product = Product.objects.get(id=id)
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
