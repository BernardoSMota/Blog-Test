from django.urls import path, include
from blog.views import index, post, creator, tags, category, post_form_view

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<slug:slug>', post, name='post'), 
    path('creator/<int:id>', creator, name='creator'), 
    path('tags/<slug:slug>', tags, name='tags'), 
    path('category/<slug:slug>', category, name='category'), \
        
    path('post/create', post_form_view, name='create_post'), 
]
