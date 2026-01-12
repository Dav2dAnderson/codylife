import uuid

from django.db import models
from django.utils.text import slugify

from users_control.models import CustomUser
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    body = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    code = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.body)[:200]
            self.slug = f"{base_slug}-{uuid.uuid4().hex[:6]}"
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Tags(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class Replies(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    code = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.body
    
    
    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
    

class Notification(models.Model):
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.to_user.username
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class Articles(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    body = models.TextField()
    code = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self):
        if not self.slug:
            base_slug = slugify(self.title)[:200]
            self.slug = f"{base_slug}-{uuid.uuid4().hex[:6]}"
        return super().save()
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

