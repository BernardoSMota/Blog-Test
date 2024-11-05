from django.apps import AppConfig
import threading
from utils.twoFAGenerator import generate_code
import os

class BloguserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogUser'

    if os.environ.get('RUN_MAIN') == 'true':
        def ready(self):
            thread = threading.Thread(target=generate_code, daemon=True)
            thread.start()