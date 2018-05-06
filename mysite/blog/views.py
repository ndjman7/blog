from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog


def index(request):
    blog_list = Blog.objects.filter(is_published=True).order_by('created_date')
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog/index.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'blog/create.html', {})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES['thumbnail']

        Blog.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
            is_published=True,
        )
        return redirect('blog:list')
