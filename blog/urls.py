# blog/urls.py
from django.urls import path
from .views import post_list, post_detail, home, create_post, create_tag

urlpatterns = [
    path('post_list/', post_list, name='post_list'),
    path('post/create/', create_post, name='create_post'),
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create_tag/', create_tag, name='create_tag'),
]
