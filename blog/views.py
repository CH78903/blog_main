from django.db.models import Q
from django.shortcuts import render, get_list_or_404, render

from .models import Post, Category

# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def detail(resquet, id):
    post = get_list_or_404(Post, id=id, status=Post.ACTIVE)


    context = {
       'post': post,
    }
    return render(resquet, 'blog/detail.html',context)