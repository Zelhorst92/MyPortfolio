from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_skills, name='skills'),
    path('add/', views.add_skill, name='add_skill'),
    path('edit/<int:skill_id>', views.edit_skill, name='edit_skill'),
]
