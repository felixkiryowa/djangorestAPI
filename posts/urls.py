from django.urls import path, re_path
from .views import (
    PostDetailAPIView,
    PostListAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView
)

app_name = 'posts'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create', PostCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='post-detail'),
    re_path(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    re_path(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]
