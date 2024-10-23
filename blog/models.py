from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=True)
    summary = models.CharField(max_length=128, null=True, blank=True)
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=False, default=None)
    cover_in_post_content = models.BooleanField(default=True, help_text='A capa somente será exibida dentro do post caso essa opção esteja marcada')
    content = HTMLField()
    published = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
