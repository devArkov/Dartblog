from django import template
from news.models import Post, Tag


register = template.Library()


@register.inclusion_tag('news/popular_news_tpl.html')
def show_popular_news(count=3):
    popular_news = Post.objects.order_by('-views')[:count]
    return {'popular_news': popular_news}


@register.inclusion_tag('news/recent_news_tpl.html')
def show_recent_news(count=3):
    recent_news = Post.objects.order_by('-created_at')[:count]
    return {'recent_news': recent_news}
