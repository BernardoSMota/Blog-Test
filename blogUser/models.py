from django.db import models
from utils import resizeImage
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    def __init__(self, *args, **kwargs):
        super(CustomUser, self).__init__(*args, **kwargs)
        self.imagem_antiga = self.profile_picture
    
    super_user_code = models.CharField(max_length=5, blank=True, help_text='Preencha este campo caso tenha uma chave para se tornar um superusuário', verbose_name='Código de superusuário')
    profile_picture = models.ImageField(upload_to='users/%Y/%m/', verbose_name='Foto de perfil', help_text='Escolha uma foto quadrada para melhor resolução')
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):    
        super().save(*args, **kwargs)  # Salva a instância normalmente primeiro
        if self.profile_picture:
            if self.imagem_antiga.name != self.profile_picture.name:
                resizeImage.resize_image(image_django=self.profile_picture, new_height=500, new_width=500)
            
        return super().save(*args, **kwargs)
        
    