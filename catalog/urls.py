from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path("", views.ProductTemplateView.as_view(), name="home"),
    path("contacts/", views.ProductView.as_view(), name="contacts"),
    path("product_list/", views.ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/create/",views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/",views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/",views.ProductDeleteView.as_view(), name="product_delete"),
]
