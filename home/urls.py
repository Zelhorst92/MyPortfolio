from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add_about, name='add_about'),
    path('edit/1', views.edit_about, name='edit_about'),
]
