from django.contrib import admin
from .models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'image_url',
        'github_link',
        'site_link',
    )

    ordering = ('name',)


admin.site.register(Project, ProjectAdmin)
