import json

from django.db.models import Count, Case, When
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status

from post.models import Post, Like
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @detail_route(methods=['post'])
    def like(self, request, pk=None):
        user = request.user
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=user)
        like.like = False if like.like else True
        like.save()
        return Response({'status': 'Performed'}, status=status.HTTP_201_CREATED)

    @detail_route(methods=['post'])
    def dislike(self, request, pk=None):
        user = request.user
        post = self.get_object()
        dislike, created = Like.objects.get_or_create(post=post, user=user)
        dislike.dislike = False if dislike.dislike else True
        dislike.save()
        return Response({'status': 'Performed'}, status=status.HTTP_201_CREATED)

    @list_route(methods=['get'])
    def get_max_posts_user(self, request, pk=None):
        post = Post.objects.all().annotate(num_likes=Count('like__like')).order_by('num_likes').last()
        return Response({'email': post.user.email}, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def get_liking_post(self, request, pk=None):
        posts = Post.objects.all().annotate(num_likes=Count(
            Case(When(like__like=True, then=1)
        ))).exclude(num_likes__gt=0).exclude(user=request.user)
        serializer = PostSerializer(data=posts, many=True)
        return Response({'posts': posts}, status=status.HTTP_200_OK)






