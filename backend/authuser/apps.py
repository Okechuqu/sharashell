from django.apps import AppConfig
from decouple import config

class AuthuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{config("APP_DIR")}.authuser'
