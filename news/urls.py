from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    # Single news operations
    path('post/<str:slug>/', views.NewsDetailView.as_view(), name='post'),
    path('add', views.NewsAddView.as_view(), name='add'),
    path('post/<str:slug>/edit/', views.NewsEditView.as_view(), name='edit'),
    path('post/<str:slug>/delete/', views.NewsDeleteView.as_view(), name='delete'),
    # News filters
    path('category/<str:slug>/', views.CategoryNewsView.as_view(), name='category'),
    path('tag/<str:slug>/', views.TagNewsView.as_view(), name='tag'),
    path('search/', views.NewsSearchView.as_view(), name='search'),
]
