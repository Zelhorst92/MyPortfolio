from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<service_id>', views.service_details, name='service_details'),
]
