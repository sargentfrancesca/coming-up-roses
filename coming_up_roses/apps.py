from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "coming_up_roses"

    def ready(self):
        import_module("coming_up_roses.receivers")
