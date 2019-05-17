from django import template
from django.conf import settings

register = template.Library()


@register.filter
def basket_total_quantity(user):
    if user.is_anonymous:
        return 0
    _items = user.basket.all()
    _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
    return _totalquantity


@register.filter
def basket_total_coster(user):
    if user.is_anonymous:
        return 0
    _items = user.basket.all()
    _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
    return _total_cost


register.filter(basket_total_quantity)
register.filter(basket_total_coster)


@register.filter
def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'
