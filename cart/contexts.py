from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """Context processor for shopping cart"""

    cart_items = []
    total = 0
    cart_item_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        cart_item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    if cart_item_count > 1:
        discount = total * Decimal(settings.COMBINATION_DISCOUNT_PERCENTAGE / 100)
    else:
        discount = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_item_count': cart_item_count,
        'combination_discount_percentage': settings.COMBINATION_DISCOUNT_PERCENTAGE,
        'price_before_vat': total - (total * Decimal(settings.VAT) / 100),
        'discount': discount,
        'net_total': (total - discount),
        'VAT': settings.VAT,
    }

    return context
