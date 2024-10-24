from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    posts = Post.objects.all().filter(published=True)
    
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/pages/index.html', context=context)

def post(request, slug):
    post = get_object_or_404(Post.objects.filter(published=True, slug=slug))
    context = {
        'post': post
    }
    return render(request, 'blog/pages/post.html', context=context)


def creator(request, id):
    posts = Post.objects.all().filter(published=True, pk=id)
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)

def tags(request, slug):
    posts = Post.objects.all().filter(published=True, tags__slug=slug)
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)