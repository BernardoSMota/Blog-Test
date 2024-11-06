from django.shortcuts import render, redirect
from blog.models import Post
from django.shortcuts import get_object_or_404
from blog.forms import PostForm
from django.http import Http404
from utils.createModels import create_category, create_tag

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
    posts = Post.objects.all().filter(published=True, creator__pk=id)
    if not posts:
        raise Http404
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)


def tags(request, slug):
    posts = Post.objects.all().filter(published=True, tags__slug=slug)
    if not posts:
        raise Http404
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)


def category(request, slug):
    posts = Post.objects.all().filter(published=True, category__slug=slug)
    if not posts:
        raise Http404
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/pages/index.html', context=context)


def post_form_view(request):
    if not request.user.is_superuser:
        raise Http404
    
    form = PostForm()
    
    if request.method == "POST":
        new_request = request.POST.copy()
        
        
        tag_id_list = create_tag(new_request) # Creating non existing tags
        category = create_category(new_request) # Creating a non existing category
        
        new_request.setlist('tags', tag_id_list)
        new_request.setlist('category', category)       
        
        form = PostForm(new_request, request.FILES)
        user = request.user
        
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = user
            post.save() 
            for tag in tag_id_list:
                post.tags.add(tag)

            return redirect('blog:index')


    return render(request, 'global/pages/form.html', {'form': form})


def post_edit_form(request, slug):
    if not request.user.is_superuser:
        raise Http404
    
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=post) 
    
    if request.method == 'POST':        
        new_request = request.POST.copy()
        
        tag_id_list = create_tag(new_request) # Creating non existing tags
        category = create_category(new_request) # Creating a non existing category
        
        new_request.setlist('tags', tag_id_list)
        new_request.setlist('category', category)

            
        form = Post(new_request, request.FILES, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save() 
            for tag in tag_id_list:
                post.tags.add(tag)
                
    return render(request, 'global/pages/form.html', {'form': form})


def delete_post(request, slug):
    if not request.user.is_superuser:
        raise Http404

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog:index')

    