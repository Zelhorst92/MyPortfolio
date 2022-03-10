from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm

# Create your views here.


def service_details(request, service_id):
    """View to show service details"""

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_details.html', context)


@login_required
def all_services(request):
    """View to show all services for sale"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to view this.')
        return redirect(reverse('home'))

    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


@login_required
def add_service(request):
    """Add a service"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

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


@login_required
def edit_service(request, service_id):
    """Edit a service"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_service(request, service_id):
    """Delete a service"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))
    try:
        service = get_object_or_404(Service, pk=service_id)
        service.delete()
        messages.success(request, 'Service successfully deleted!')
        return redirect(reverse('services'))
    except Exception as e:
        messages.error(request, f'Something went terribly wrong; {e}')
        return HttpResponse(content=e, status=400)
