from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings

from services.models import Service
from skills.models import Skill
from projects.models import Project
from .models import AboutUser
from .forms import AboutForm, ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.


def index(request):
    """View to return index page"""
    allows_message = settings.CONTACT_FORM_ENABLED
    if request.method == 'POST':
        if allows_message:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject'],
                body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'subject': form.cleaned_data['subject'],
                    'message': form.cleaned_data['message'],
                }
                full_message = "\n".join(body.values())
                try:
                    send_mail(
                        subject,
                        full_message,
                        settings.EMAIL_HOST_USER,
                        [settings.DEFAULT_FROM_EMAIL],
                        fail_silently=False)
                    messages.success(request, 'The message is successfully send! \
                        Thank you for your message,\
                             you will receive a reply soon!')
                    return redirect('home')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                messages.error(request, 'Failed to send the message. \
                    Are all fields filled in correctly?')
                return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'The siteowner does not allow messages to be sent at this time'
                )
            return redirect(reverse('home'))
    else:
        form = ContactForm()

    about_user = AboutUser.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.get_queryset().order_by('id')
    service_paginator = Paginator(services, 2)
    page_number = request.GET.get('page')
    page = service_paginator.get_page(page_number)

    template = 'home/index.html'
    context = {
        'about_user': about_user,
        'projects': projects,
        'services': services,
        'skills': skills,
        'service_paginator': service_paginator,
        'page': page,
        'page_number': page_number,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_about(request):
    """Add the about information"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'About information succesfully added!')
            return redirect(reverse('site_manager'))
        else:
            messages.error(request, 'Failed to add about information. \
                Are all fields filled in correctly?')
    else:
        form = AboutForm()

    template = 'home/add_about.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


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
            messages.success(
                request, 'The about information is successfully edited!')
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
