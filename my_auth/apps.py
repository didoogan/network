from django.apps import AppConfig


class MyAuthConfig(AppConfig):
    name = 'my_auth'
    verbose_name = 'My_auth Application'

    def ready(self):
        import my_auth.signals
