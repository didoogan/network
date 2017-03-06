from django.conf import settings
from django.db import models


class PostModel(models.Model):
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
