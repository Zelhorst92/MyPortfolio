from django.shortcuts import render

# Create your views here.


def skills(request):
    skills = Skill.objects.all()

    context = {
        'skills': skills,
    }

    return (render(request, 'skills/skills.html', context))
