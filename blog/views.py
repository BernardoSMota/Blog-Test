from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from blog.forms import PostForm


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


def category(request, slug):
    posts = Post.objects.all().filter(published=True, category__slug=slug)
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)


def post_form_view(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')


    return render(request, 'blog/pages/form.html', {'form': form})