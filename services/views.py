from django.shortcuts import render, get_object_or_404
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
    form = ServiceForm()
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)