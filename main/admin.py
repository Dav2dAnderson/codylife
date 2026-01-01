from django.contrib import admin

from .models import Tags, Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['body', 'created_date']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']