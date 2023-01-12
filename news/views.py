from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Category, Tag
from django.db.models import F
from .forms import NewsForm
from .filters import MewsFilter
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        return context


class CategoryNewsView(ListView):
    template_name = 'news/category_news_list.html'
    context_object_name = 'news'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class TagNewsView(ListView):
    template_name = 'news/tag_news_list.html'
    context_object_name = 'news'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class NewsAddView(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add.html'
    success_url = reverse_lazy('news')


class NewsEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewsForm
    template_name = 'news/edit.html'
    success_url = reverse_lazy('news')


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_confirm_delete.html'
    success_url = reverse_lazy('news')


class NewsSearchView(ListView):
    model = Post
    template_name = 'news/news_search.html'
    ordering = ['-created_at']
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MewsFilter(self.request.GET, queryset=self.get_queryset())
        return context
