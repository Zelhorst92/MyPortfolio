from django.shortcuts import render
from services.models import Service
from .models import Skill, PreviousProject


# Create your views here.


def index(request):
    """View to return index page"""
    skills = Skill.objects.all()
    PreviousProjects = PreviousProject.objects.all()
    services = Service.objects.all()

    context = {
        'skills': skills,
        'PreviousProjects': PreviousProjects,
        'services': services,
    }

    return render(request, 'home/index.html', context)
