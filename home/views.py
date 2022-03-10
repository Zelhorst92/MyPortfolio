from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
    about_user = AboutUser.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    services = Service.objects.get_queryset().order_by('id')
    service_paginator = Paginator(services, 3)
    page_number = request.GET.get('page')
    page = service_paginator.get_page(page_number)

    context = {
        'about_user': about_user,
        'projects': projects,
        'services': services,
        'skills': skills,
        'service_paginator': service_paginator,
        'page': page,
        'page_number': page_number,
    }

    return render(request, 'home/index.html', context)


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "main/contact.html", {'form':form})


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
