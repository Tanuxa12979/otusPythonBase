from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list', views.products_list, name='products_list'),
    path('product/<int:id>/', views.product, name='product'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:id_product>/edit', views.edit_product, name='edit_product'),
]
