from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Service
# Create your views here.


def view_cart(request):
    """A view to view the contents in the shopping cart"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of a service to the shopping cart"""

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added {service.name} to the cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {service.name} to the cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """change the quantity of a service in the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove a service from the shopping cart"""

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exeption as e:
        return HttpResponse(status=500)
