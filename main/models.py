from django.db import models
from django.utils.text import slugify

from users_control.models import CustomUser
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.author.username

    def save(self):
        if not self.slug:
            self.slug = slugify(self.body)
        return super().save()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Tags(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    