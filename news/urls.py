from django.urls import path


from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('post/<str:slug>/', views.NewsDetailView.as_view(), name='post'),
    path('add', views.NewsAddView.as_view(), name='add'),
    path('category/<str:slug>/', views.CategoryNewsView.as_view(), name='category'),
    path('tag/<str:slug>/', views.TagNewsView.as_view(), name='tag'),
]
