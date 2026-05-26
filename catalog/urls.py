from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path("", views.ProductTemplateView.as_view(), name="home"),
    path("contacts/", views.ProductView.as_view(), name="contacts"),
    path("product_list/", views.ProductListView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/",
        cache_page(60 * 5)(views.ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "product/unpublish/",
        views.ProductUnpublishView.as_view(),
        name="product_unpublish",
    ),
    path(
        "category/<int:category_id>/",
        views.product_by_category_view,
        name="product_by_category",
    ),
]
