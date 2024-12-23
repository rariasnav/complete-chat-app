from django.apps import AppConfig


class SeoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.seo'
    
    def ready(self):
        import api.seo.signals