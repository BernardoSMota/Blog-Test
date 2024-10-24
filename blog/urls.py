from django.urls import path, include
from blog.views import index, post, creator, tags

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<slug:slug>', post, name='post'), # ALTERAR E COLOCAR UM SLUG
    path('creator/<int:id>', creator, name='creator'), # ALTERAR E COLOCAR UM SLUG
    path('tags/<slug:slug>', tags, name='tags'), # ALTERAR E COLOCAR UM SLUG
]
