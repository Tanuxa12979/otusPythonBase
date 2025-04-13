from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store_app/products_list.html", context=context)


def product(request, id: int):
    #product = Product.objects.get(id=id)
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render(request, "store_app/product.html", context=context)