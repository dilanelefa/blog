from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import commonmark
from blog_app.models import Post


def index(request: HttpRequest):
    posts = Post.objects.all()
    if request.GET.get('query'):
        query = request.GET.get('query')
        posts = posts.filter(title__icontains=query)

    posts = posts.order_by('-update_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/index.html', context)


def show_post(request: HttpRequest, post_id: int, slug: str = None):
    post = Post.objects.get(pk=post_id)
    post.content = commonmark.commonmark(post.content)

    # Don't apply post.save()
    context = {
        'post': post
    }
    return render(request, 'blog_app/single.html', context)
