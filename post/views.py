from django.db.models import Count
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

    @detail_route(methods=['post'])
    def get_max_posts_user(self, request, pk=None):
        post = Post.objects.all().annotate(num_likes=Count('likes')).order_by('num_likes').last()




