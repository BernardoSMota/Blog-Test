from django.urls import path
from blog.views import index, post, creator, tags, category, post_form_view, post_edit_form, delete_post

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('creator/<int:id>', creator, name='creator'), 
    path('tags/<slug:slug>', tags, name='tags'), 
    path('category/<slug:slug>', category, name='category'), \
        
    path('posts/<slug:slug>', post, name='post'), 
    path('post/create', post_form_view, name='create_post'), 
    path('post/<slug:slug>/edit/', post_edit_form, name='edit_post'), 
    path('post/<slug:slug>/delete/', delete_post, name='delete_post'), 
]
