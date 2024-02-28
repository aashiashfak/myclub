# base/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.http import HttpRequest

@receiver(post_save, sender=User)
def new_user_created(sender, instance, created, **kwargs):
    if created:
        request = HttpRequest()
        print("New User Created")
