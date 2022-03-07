from django.shortcuts import render, get_object_or_404

from .models import UserProfile
# Create your views here.


def profile(request):
    """Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/dashboard.html'
    context = {}

    return render(request, template, context)
