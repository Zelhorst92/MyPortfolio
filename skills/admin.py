from django.contrib import admin
from .models import Skill

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_url',
        'hidden',
    )

    ordering = ('name',)


admin.site.register(Skill, SkillAdmin)
