from django.contrib import admin
from .models import PreviousProject

# Register your models here.


class PreviousProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'image_url',
        'github_link',
        'site_link',
    )

    ordering = ('name',)


admin.site.register(PreviousProject, PreviousProjectAdmin)