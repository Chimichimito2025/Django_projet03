from django.shortcuts import render
from store.models import Product
from django.views.generic import ListView

class ProductListView(ListView):
    model=Product
    template_name="list_products.html"
    context_object_name="products"