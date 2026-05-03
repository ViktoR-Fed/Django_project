from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path("", views.ProductTemplateView.as_view(), name="home"),
    path("contacts/", views.ProductView.as_view(), name="contacts"),
    path("product_list/", views.ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
