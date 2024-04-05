from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard.index'),
    path('posts/', views.list_post, name='post.index'),
    path('posts/create/', views.create_post, name='post.create'),
    path('imageUpload/', views.image_upload, name='image_upload')
]
