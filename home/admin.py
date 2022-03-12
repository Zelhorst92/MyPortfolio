from django.contrib import admin
from .models import AboutUser
# Register your models here.


class AboutUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession',)


admin.site.register(AboutUser, AboutUserAdmin)
