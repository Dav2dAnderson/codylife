from django.contrib import admin

from .models import CustomUser, Technologies
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'image_tag']


@admin.register(Technologies)
class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ['name', ]