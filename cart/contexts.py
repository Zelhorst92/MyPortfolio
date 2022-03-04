from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    cart_item_count = 0

    if cart_item_count > 1:
        net_total = total * Decimal(
            settings.COMBINATION_DISCOUNT_PERCENTAGE / 100)
    else:
        net_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_item_count': cart_item_count,
        'combination_discount_percentage': settings.COMBINATION_DISCOUNT_PERCENTAGE,
        'net_total': net_total,
    }

    return context
