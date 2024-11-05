from pathlib import Path
from django.conf import settings
from PIL import Image # type: ignore


# def resize_image(path_image_django, new_width=800, optimize=True, quality=60):
#     image_pillow = Image.open(path_image_django)
#     original_width, original_height = image_pillow.size

#     if original_width <= new_width:
#         image_pillow.close()
#         return image_pillow

#     new_height = round(new_width * 1080 / 1920)

#     new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

#     new_image.save(
#         path_image_django,
#         optimize=optimize,
#         quality=quality,
#     )

#     return new_image


def resize_image(image_django, new_width=800, new_height=None, optimize=True, qualiy= 70):
    image_path = image_django.path
    img = Image.open(image_path)

    if not new_height:
        new_height = round(new_width * 1080 / 1920)     
        
    new_size = (new_width, new_height)
        
    
    img = img.resize(new_size, Image.LANCZOS)

    img.save(image_path, optimize=optimize, qualiy=qualiy)
    
    return img