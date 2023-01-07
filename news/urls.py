from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    # News operations
    path('post/<str:slug>/', views.NewsDetailView.as_view(), name='post'),
    path('add', views.NewsAddView.as_view(), name='add'),
    path('post/<str:slug>/edit/', views.NewsEditView.as_view(), name='edit'),
    # News filters
    path('category/<str:slug>/', views.CategoryNewsView.as_view(), name='category'),
    path('tag/<str:slug>/', views.TagNewsView.as_view(), name='tag'),
]
