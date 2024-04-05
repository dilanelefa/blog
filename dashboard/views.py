from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_exempt

from blog_app.models import Post, Image
from dashboard.forms import CreatePostForm
from user.middlewares import auth


@auth
def index(request: HttpRequest):
    return render(request, 'dashboard/index.html')


@auth
def list_post(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/list.html', context)


@auth
def create_post(request: HttpRequest):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            slug = slugify(form.cleaned_data['title'])
            author = request.user
            post = Post.objects.create(title=form.cleaned_data['title'], slug=slug, author=author, content=form.cleaned_data['content'])
            post.description = form.cleaned_data['description']
            post.thumbnail = form.cleaned_data['thumbnail']
            post.save()

            return redirect('post.index')

    return render(request, 'dashboard/create_post.html', {'form': form})

@csrf_exempt
def image_upload(request):
    print(request)
    if request.method == 'OPTIONS' or request.method == "POST":
        image = Image.objects.create(image=request.FILES['image'])
        # image.save()

        return JsonResponse({"data": {"filePath": image.image.url}}, status=200)
    return JsonResponse({'error': 'GET method not allowed'}, status=405)
