from django.utils.text import slugify
from random import SystemRandom
import string

def random_letters(size=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase+ string.digits, 
        k=size
    ))

def slugfy_new(text, size=5):
    end = ''.join(SystemRandom().choices(string.ascii_lowercase+ string.digits, k=size))
    return f'{slugify(text)}-{end}'
