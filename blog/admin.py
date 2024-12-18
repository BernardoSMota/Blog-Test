from django.contrib import admin
from blog.models import Post, Tag, Category#, Likes
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id','title', 'summary', 'creator', 'published',
    list_editable = 'published',
    search_fields = 'title', 'creator',
    # readonly_fields = 'creator', 'created_at', # VOLTAR AO NORMAL DEPOIS
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = 'tags',
    
@admin.register(Tag)
class TitleAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug',
    search_fields = 'title',
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug',
    search_fields = 'title',
    prepopulated_fields = {'slug': ('title',)}
