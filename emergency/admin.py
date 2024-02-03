from django.contrib import admin
from django.utils.html import format_html

from .models import EmergencyCategory, Emergency


# Register your models here.
@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'show_image')
    search_fields = ('id',)\

    def show_image(self, obj):
        return format_html('<img src="{}" width="60px" height="60px" style="border-radius: 20%" />', obj.image.url)

    show_image.short_description = 'Imagen'


@admin.register(EmergencyCategory)
class EmergencyCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_image')
    search_fields = ('name',)

    def show_image(self, obj):
        return format_html('<img src="{}" width="60px" height="60px" style="border-radius: 20%" />', obj.image.url)

    show_image.short_description = 'Imagen'
