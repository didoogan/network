import clearbit

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework import status

from rest_framework.response import Response

clearbit.key = settings.CLEARBIT_SECRET_KEY


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if instance.approved:
        return
    if created:
        person = clearbit.Person.find(email=instance.email, stream=True)
        if not person:
            return
        if person:
            instance.first_name = person['name']['givenName']
            instance.last_name = person['name']['familyName']
            instance.approved = True
            instance.save(update_fields=['first_name', 'last_name', 'approved'])





