from django.contrib import admin
from .models import Skill, Category

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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
