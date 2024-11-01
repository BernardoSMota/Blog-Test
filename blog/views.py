from django.shortcuts import render, redirect
from blog.models import Post, Tag, Category
from django.shortcuts import get_object_or_404
from blog.forms import PostForm
from django.http import Http404


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
        
        # Creating non existing tags and changing the request
        tag_id_list = []
        tags = new_request.getlist('tags', [])        
        for tag in tags:
            if not tag.isnumeric():
                tag, created = Tag.objects.get_or_create(title=tag) 
                tag_id_list.append(str(tag.id))
            else:
                tag_id_list.append(str(tag))
        
        new_request.setlist('tags', tag_id_list)
        
        # Creating a non existing category and changing the request
        category = new_request.get('category')
        if not category.isnumeric():
            category, created = Category.objects.get_or_create(title=category)
            category_id = [str(category.id)]
            new_request.setlist('category', category_id)       
        else:
            new_request.setlist('category', category)       
        
        
        
        form = PostForm(new_request, request.FILES)
        user = request.user
        
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = user
            post.save() 
            for tag in tag_id_list:
                post.tags.add(tag)

            return redirect('blog:index')


    return render(request, 'global/pages/form.html', {'form': form})