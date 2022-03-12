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
    service_count = 0
    discount = 0

    for item_id, quantity in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        cart_item_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })
    """
    Only apply discount if multiple services are being bought
    """
    for service.sku in cart.items():
        service_count += 1
        if service_count > 1:
            discount = total * Decimal(
                settings.COMBINATION_DISCOUNT_PERCENTAGE / 100)

    net_total = total - discount
    vat = net_total * Decimal(settings.VAT_PERCENTAGE) / 100

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_item_count': cart_item_count,
        'combination_discount_percentage':
            settings.COMBINATION_DISCOUNT_PERCENTAGE,
        'vat': vat,
        'net_total': net_total,
        'discount': discount,
        'vat_percentage': settings.VAT_PERCENTAGE,
    }

    return context
