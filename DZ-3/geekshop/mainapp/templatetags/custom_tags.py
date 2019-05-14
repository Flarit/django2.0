from django import template

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
