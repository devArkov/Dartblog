from django_filters import FilterSet
from .models import Post


class MewsFilter(FilterSet):
    class Meta:
        model = Post
        # fields = ('title', 'content', 'category', 'tags')
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
            'author': ['icontains'],
            'created_at': ['gt'],
        }
