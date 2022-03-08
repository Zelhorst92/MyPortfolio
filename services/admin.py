from django.contrib import admin
from .models import Service, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('id',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
