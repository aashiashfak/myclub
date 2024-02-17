# base/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpRequest

@receiver(post_save, sender=User)
def new_user_created(sender, instance, created, **kwargs):
    if created:
        request = HttpRequest()
        messages.success(request,'Your account was created successfully. Please log in.')
        print("New User Created")
