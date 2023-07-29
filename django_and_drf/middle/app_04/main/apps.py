from django.apps import AppConfig
from django.dispatch import Signal

from main.utils import send_activation_notification

user_registered = Signal(providing_args=['instance'])

def user_registered_dispatcher(sender: str, **kwargs) -> None:
    send_activation_notification(kwargs['instance'])

user_registered.connect(user_registered_dispatcher)


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    verbose_name = 'Астро Новости'
