from django.urls import path


from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('category/<str:slug>/', views.category, name='category'),
    path('post/<str:slug>/', views.post, name='post'),
]
