from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Category', unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Slug')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField(blank=True, verbose_name='Published')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0, verbose_name='Views count')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
