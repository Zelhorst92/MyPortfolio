from django.contrib import admin
from .models import PreviousProject, AboutUser

# Register your models here.

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


admin.site.register(PreviousProject, PreviousProjectAdmin)
admin.site.register(AboutUser, AboutUserAdmin)
