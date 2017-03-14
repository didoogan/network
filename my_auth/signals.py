import clearbit

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if instance.approved:
        return
    if created:
        clearbit.key = settings.CLEARBIT_SECRET_KEY
        person = clearbit.Person.find(email=instance.email, stream=True)
        if person:
            instance.first_name = person['name']['givenName']
            instance.last_name = person['name']['familyName']
            instance.approved = True
            instance.save()





