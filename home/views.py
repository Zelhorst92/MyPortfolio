from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from services.models import Service
from skills.models import Skill
from .models import AboutUser, PreviousProject
from .forms import AboutForm


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


@login_required
def edit_about(request):
    """Edit the about information"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    about_id = 1
    about = get_object_or_404(AboutUser, pk=about_id)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'The about information is successfully edited!')
            return redirect(reverse('site_manager'))
        else:
            messages.error(request, 'Failed to edit the about information. \
                Are all fields filled in correctly?')
    else:
        form = AboutForm(instance=about)
        messages.info(request, 'You are editing the about information')

    template = 'home/edit_about.html'
    context = {
        'form': form,
        'about': about,
    }

    return render(request, template, context)