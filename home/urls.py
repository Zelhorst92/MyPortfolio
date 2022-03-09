from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('edit/1', views.edit_about, name='edit_about'),
]
