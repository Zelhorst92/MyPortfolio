from django.shortcuts import render
from .models import Skill, PreviousProject

# Create your views here.


def index(request):
    """View to return index page"""
    skills = Skill.objects.all()
    PreviousProjects = PreviousProject.objects.all()

    context = {
        'skills': skills,
        'PreviousProjects': PreviousProjects,
    }

    return render(request, 'home/index.html', context)
