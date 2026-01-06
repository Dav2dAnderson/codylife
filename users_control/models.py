from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe

import uuid
# Create your models here.


class EmailVerification(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField("Technologies", blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.username

    def image_tag(self):
        if self.picture:
            return mark_safe(
                f'<img src="{self.picture.url}" width="75" height="100" '
                'style="object-fit:cover;border-radius:6px;" />'
            )
        return "No Image"

    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Technologies(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'


