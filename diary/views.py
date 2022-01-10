from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    details = {'post': post_detail}
    return render(request, 'detail.html', details)

def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.contexts = request.POST['body']
        post.photo = request.FILES.get('photo')
        post.save()
        return redirect('/')
    else:
        return render(request, 'error.html')

def edit(request, post_id):
    post_edit = get_object_or_404(Post, id=post_id)
    edits = {'post': post_edit}
    return render(request, 'edit.html', edits)

def update(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        if request.FILES.get('photo') is not None:
            post.title = request.POST['title']
            post.contexts = request.POST['body']
            post.photo = request.FILES['photo']
            post.save()
        else:
            post.title = request.POST['title']
            post.contexts = request.POST['body']
            post.save()
    else:
        return render(request, 'error.html')
    return redirect('/')

def delete(request, post_id):
    post_delete = Post.objects.get(id=post_id)
    post_delete.delete()
    return redirect('/')
