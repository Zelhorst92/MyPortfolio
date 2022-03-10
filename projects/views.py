from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

# Create your views here.


@login_required
def all_projects(request):
    """View to show all the projects in the database"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to view this.')
        return redirect(reverse('home'))

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return (render(request, 'projects/projects.html', context))

@login_required
def add_project(request):
    """Add a projects"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project succesfully added!')
            return redirect(reverse('projects'))
        else:
            messages.error(request, 'Failed to add project. \
                Are all fields filled in correctly?')
    else:
        form = ProjectForm()

    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, project_id):
    """Edit a project"""
    if not request.user.is_superuser:
        messages.error(request, 'You have no permission to do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project successfully edited!')
            return redirect(reverse('projects'))
        else:
            messages.error(request, 'Failed to edit project. \
                Are all fields filled in correctly?')
    else:
        form = ProjectForm(instance=project)
        messages.info(request, f'You are editing project {project.name}')

    template = 'projects/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)
