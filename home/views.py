from django.shortcuts import render
from django.core.paginator import Paginator
from services.models import Service
from .models import Skill, PreviousProject


# Create your views here.


def index(request):
    """View to return index page"""
    skills = Skill.objects.all()
    PreviousProjects = PreviousProject.objects.all()
    services = Service.objects.all()

    service_paginator = Paginator(services, 3)

    page_number = request.GET.get('page')

    page = service_paginator.get_page(page_number)

    context = {
        'skills': skills,
        'PreviousProjects': PreviousProjects,
        'services': services,
        'service_paginator': service_paginator,
        'page': page,
        'page_number': page_number,
    }

    return render(request, 'home/index.html', context)
