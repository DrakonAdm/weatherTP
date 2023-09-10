from django.apps import AppConfig


class TerminatorWeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'terminatorWeather'

    def ready(self):
        from . import scheduler
        scheduler.start()
