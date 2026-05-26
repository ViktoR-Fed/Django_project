from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Product


class ProductService:

    @staticmethod
    def get_product_from_cache():
        """Получение данных по продуктам из кэша, если кэш пуст, получает данные из базы данных."""
        if not CACHE_ENABLED:
            return Product.objects.all()

        key = "products_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    @staticmethod
    def get_products_by_category(category_id):
        return Product.objects.filter(category_id=category_id)
