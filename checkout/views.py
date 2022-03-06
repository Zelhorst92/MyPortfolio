import os
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

if os.path.exists('env.py'):
    import env

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in the cart!")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('stripe_public_key'),
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
