from django.apps import AppConfig


class ClientConfig(AppConfig):
    name = 'client'
    verbose_name = 'Clientes'

    def ready(self):
        from . import signals  # noqa: F401
