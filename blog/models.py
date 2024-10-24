from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from utils import slugfy, resizeImage
from PIL import Image


class Tag(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True, default=None)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy.slugfy_new(self.title)
            
        return super().save(*args, **kwargs)
        


class Post(models.Model):
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.imagem_antiga = self.cover
        
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy.slugfy_new(self.title)
            
        
        current_cover_name = str(self.cover.name)
        super().save(*args, **kwargs)  # Salva a instância normalmente primeiro

        if self.cover:
            if self.imagem_antiga.name != self.cover.name:
                resizeImage.resize_image(self.cover)
            
        return super().save(*args, **kwargs)
        