from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm

# Create your views here.


def all_services(request):
    """View to show all services for sale"""

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_details(request, service_id):
    """View to show service details"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_details.html', context)

def add_service(request):
    """Add a service"""
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service succesfully added!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to add service. \
                Are all fields filled in correctly?')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, service_id):
    """Edit a service"""
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service successfully edited!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to edit service. \
                Are all fields filled in correctly?')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing service {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)
