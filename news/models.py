from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Category', unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Slug')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ['title']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField(blank=True, verbose_name='Published')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0, verbose_name='Views count')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})
