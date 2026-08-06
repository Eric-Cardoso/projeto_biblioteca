from django.apps import AppConfig


class LoanConfig(AppConfig):
    name = 'loan'
    verbose_name = 'Empréstimos'

    def ready(self):
        from . import signals
