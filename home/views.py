from django.shortcuts import render
from .models import Skill

# Create your views here.


def index(request):
    """View to return index page"""
    skills = Skill.objects.all()

    context = {
        'skills': skills,
    }

    return render(request, 'home/index.html', context)
