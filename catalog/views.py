from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class ProductTemplateView(TemplateView):
    model = Product
    template_name = "home.html"

class ProductView(TemplateView):
    model = Product
    template_name = "contacts.html"

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"