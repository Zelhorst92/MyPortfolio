from django.contrib import admin
from .models import Skill, Category, PreviousProject, AboutUser

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'image',
        'image_url',
    )

    ordering = ('name',)


class PreviousProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'image_url',
    )

    ordering = ('name',)


class AboutUserAdmin(admin.ModelAdmin):
    list_display = (
    'full_name',
    'profession',
    )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(PreviousProject, PreviousProjectAdmin)
admin.site.register(AboutUser, AboutUserAdmin)
