from django.dispatch import receiver
from .signal import new_instance_signal
from django.db.models.signals import post_delete
from . models import Products


@receiver(new_instance_signal, sender=Products)
def new_instance_handler(sender, instance, **kwargs):
    hai = kwargs.get('hai')
    print(f"{hai} New instance of {sender.__name__} created: {instance}")

@receiver(post_delete, sender=Products)
def delete_handler(sender, instance, **kwargs):
    print(f"instance: {instance} deleted from model: {sender.__name__}")

# new_instance_signal.connect(new_instance_handler , sender=Products)
# post_delete.connect(delete_handler, sender=Products)


