from django.apps import AppConfig
from decouple import config

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{config("UI_DIR")}.blog'
