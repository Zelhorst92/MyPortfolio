from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Skill
from .forms import SkillForm

# Create your views here.


@login_required
def all_skills(request):
    """View to show all the skills in the database"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to view this.')
        return redirect(reverse('home'))

    skills = Skill.objects.all()

    context = {
        'skills': skills,
    }

    return (render(request, 'skills/skills.html', context))


@login_required
def add_skill(request):
    """Add a skill"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill succesfully added!')
            return redirect(reverse('skills'))
        else:
            messages.error(request, 'Failed to add skill. \
                Are all fields filled in correctly?')
    else:
        form = SkillForm()

    template = 'skills/add_skill.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_skill(request, skill_id):
    """Edit a skill"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill successfully edited!')
            return redirect(reverse('skills'))
        else:
            messages.error(request, 'Failed to edit skill. \
                Are all fields filled in correctly?')
    else:
        form = SkillForm(instance=skill)
        messages.info(request, f'You are editing skill {skill.name}')

    template = 'skills/edit_skill.html'
    context = {
        'form': form,
        'skill': skill,
    }

    return render(request, template, context)


@login_required
def delete_skill(request, skill_id):
    """Delete a skill"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))
    try:
        skill = get_object_or_404(Skill, pk=skill_id)
        skill.delete()
        messages.success(request, 'Skill successfully deleted!')
        return redirect(reverse('skills'))
    except Exception as e:
        messages.error(request, f'Something went terribly wrong; {e}')
        return HttpResponse(content=e, status=400)
