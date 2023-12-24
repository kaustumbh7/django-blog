from django.urls import path
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    path('api/blogs', BlogPostList.as_view(), name='blog-list'),
    path('api/blog/<int:pk>', BlogPostDetail.as_view(), name='blog-details')
]
