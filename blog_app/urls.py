from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog.index'),
    path('single/<slug:slug>-<int:post_id>/', views.show_post, name='blog.detail')
]
