from django.contrib import admin
from blog.models import Post, Tag
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'summary', 'owner', 'published',
    list_editable = 'published',
    search_fields = 'title', 'owner',
    readonly_fields = 'owner', 'created_at',
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Tag)
class TitleAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug',
    search_fields = 'title',
    prepopulated_fields = {'slug': ('title',)}