from django.db import models
from django.conf import settings

from post.models import Post


class Like(models.Model):
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return self.user.email
