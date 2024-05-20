from django.urls import path
from .views import BlogDetail, BlogInfo

urlpatterns = [
    path("detail/", BlogDetail.as_view(), name='blog'),
    path("my-blogs/", BlogInfo.as_view(), name='blog-info own'),

    path("my-blogs/<int:pk>/", BlogInfo.as_view(), name='blog-info'),
]