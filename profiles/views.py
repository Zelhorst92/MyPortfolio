from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from home.models import AboutUser
from checkout.models import Order
# Create your views here.


@login_required
def profile(request):
    """Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your information has been updated successfully!')
        else:
            messages.error(
                request, 'Failed to update information. \
                    Are all required fields filled in correctly?')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    template = 'profiles/dashboard.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number { order_number }. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def site_manager(request):
    """Display the site management dashboard"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to view this.')
        return redirect(reverse('home'))

    about_user = AboutUser.objects.all()
    template = 'profiles/sitemanager.html'
    context = {
        'about_user': about_user
        }
    return render(request, template, context)
