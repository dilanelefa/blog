from user.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.fields.CharField(max_length=128)
    content = models.fields.TextField()
    description = models.CharField(max_length=64)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='posts_thumbnails')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.fields.DateTimeField(default=timezone.now)
    update_at = models.fields.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
