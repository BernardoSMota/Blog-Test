import random
import string
from time import sleep
from django.core.cache import cache
from utils.sendMessage import TFA

current_code = None

def generate_code(size=5, sleep_time=30):
    global current_code
    while True:
        current_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
        print(f"Novo código gerado: {current_code}")
        TFA(code=current_code)
        cache.set('current_code', current_code, timeout=sleep_time)
        sleep(sleep_time)
    