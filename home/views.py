from django.shortcuts import render
from django.core.paginator import Paginator
from services.models import Service
from skills.models import Skill
from .models import AboutUser, PreviousProject


# Create your views here.


def index(request):
    """View to return index page"""
    about_user = AboutUser.objects.all()
    skills = skills = Skill.objects.all()
    PreviousProjects = PreviousProject.objects.all()
    services = Service.objects.get_queryset().order_by('id')
    service_paginator = Paginator(services, 3)
    page_number = request.GET.get('page')
    page = service_paginator.get_page(page_number)

    context = {
        'about_user': about_user,
        'PreviousProjects': PreviousProjects,
        'services': services,
        'skills': skills,
        'service_paginator': service_paginator,
        'page': page,
        'page_number': page_number,
    }

    return render(request, 'home/index.html', context)
