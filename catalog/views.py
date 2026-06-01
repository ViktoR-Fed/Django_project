from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from catalog.services import ProductService


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/home.html"


class ProductView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return ProductService.get_product_from_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем категории в контекст
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductUnpublishView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs["pk"])
        if request.user.has_perm("catalog.can_unpublish_product"):
            product.publication_status = False
            product.save()
            return redirect("catalog:product_list")
        else:
            return HttpResponseForbidden("У вас нет прав на выполнение этого действия.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def post(self, request, *args, **kwargs):
        products = get_object_or_404(Product, pk=kwargs["pk"])
        if (
            request.user.has_perm("catalog.can_unpublish_product")
            or request.user == products.owner
        ):
            return redirect("catalog:product_delete", pk=kwargs["pk"])
        else:
            return HttpResponseForbidden("У вас нет прав на выполнение этого действия.")


def product_by_category_view(request, category_id):
    categories = Category.objects.all()
    products = ProductService.get_products_by_category(category_id)
    return render(
        request,
        "catalog/product_list.html",
        {
            "products": products,
            "categories": categories,
            "selected_category_id": category_id,
        },
    )
