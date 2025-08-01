from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogDeleteView, BlogUpdateView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>',BlogDetailView.as_view(), name='post_detail'),
    path('',BlogListView.as_view(), name='home')
]