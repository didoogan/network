from django.conf import settings
from django.db import models


class Post(models.Model):
    text = models.TextField(blank=True, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user.email


class Like(models.Model):
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return self.user.email
