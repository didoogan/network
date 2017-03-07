from django.conf import settings
from django.db import models


class Post(models.Model):
    text = models.TextField(blank=True, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email
