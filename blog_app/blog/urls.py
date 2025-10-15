from django.urls import path
from .views import BlogDetailView, BlogListView


urlpatterns = [
    path('post/<int:pk>',BlogDetailView.as_view(), name='detail_post'),
    path('',BlogListView.as_view(), name='home')
]