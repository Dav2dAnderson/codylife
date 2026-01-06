from django.contrib import admin

from .models import Tags, Post, Replies, Notification, Articles
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['body', 'created_date']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Replies)
class RepliesAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_date']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'body', 'created_date']


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']