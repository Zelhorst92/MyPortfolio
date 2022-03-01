from django.shortcuts import render
from .models import Skill, PreviousProject
from services.models import Service

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
