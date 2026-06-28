from .models import Product
from django.core.cache import cache

def get_products_by_category(category_id=None, only_published=True):
    """
    Возвращает список продуктов в указанной категории.
    Если category_id=None — возвращает все продукты.
    only_published=True — фильтрует только опубликованные продукты.
    """
    cache_key = f'products_by_category_{category_id}_{only_published}'
    products = cache.get(cache_key)

    if products is not None:
        return products

    qs = Product.objects.all()

    if only_published:
        qs = qs.filter(is_published=True)

    if category_id is not None:
        qs = qs.filter(category_id=category_id)

    products = list(qs.select_related('category', 'owner'))  # select_related для оптимизации запросов
    cache.set(cache_key, products, 60)  # кешируем на 60 секунд

    return products