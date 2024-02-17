from django.apps import AppConfig


class MyclubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myclub'

    def ready(self):
        import myclub.reciever