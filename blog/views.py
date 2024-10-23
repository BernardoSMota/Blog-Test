from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().filter(published=True)
    
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/pages/index.html', context=context)

def post(request):
    return render(request, 'blog/pages/post.html')