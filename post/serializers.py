from django.db.models import Sum
from rest_framework import serializers

from my_auth.api.serializers import MyUserSerializer
from post.models import Post
from .models import Like


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        # likes = Like.objects.filter(post=obj).aggregate(Sum('like'))['like__sum']
        likes = Like.objects.filter(post=obj, like=True).count()
        if not likes:
            likes = 0
        return likes

    def get_dislikes(self, obj):
        # unlikes = Like.objects.filter(post=obj).aggregate(Sum('unlike'))['unlike__sum']
        unlikes = Like.objects.filter(post=obj, dislike=True).count()
        if not unlikes:
            unlikes = 0
        return unlikes
